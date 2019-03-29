# -*- coding: utf-8 -*-

from django.shortcuts import HttpResponse, HttpResponseRedirect, render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from app.bitacora.models import Bitacora
from app.investigacion.models import * 
from django.forms.models import modelformset_factory
from django.views.decorators.csrf import csrf_exempt

from app.entrevista.controllerpersona import ControllerPersona
from app.persona.form_functions import *
from django.conf import settings
import datetime
import xlrd
import os
import json
from django.db.models import Q
from app.reportes.services import ServiceReporte
from reportlab.pdfgen import canvas

login_required(login_url='/login', redirect_field_name=None)
@user_passes_test(lambda u: u.is_staff, login_url='/', redirect_field_name=None)
def panel(request):
	'''
		NOTA: Al modificar código en esta función, revisar también app.reportes.servcies, pues ahí también
		se generan los reportes que se envian por correo. El código es similar.
	'''
	#Fix por pixeles en Chrome (input-group-addon de bootstrap)
	es_chrome = 'Chrome' in request.META['HTTP_USER_AGENT']
	page = 'reportes'
	sr = ServiceReporte()

	#para SEARCH sidebar
	empresas_select = Compania.objects.filter(status=True, es_cliente=True).order_by('nombre')
	status_select = Investigacion.STATUS_GRAL_OPCIONES
	filtros_json = request.session.get('filtros_search_reportes', None)

	if filtros_json != None:
		if not len(filtros_json['compania_id']) and not len(filtros_json['compania_nombre']) and not len(filtros_json['contacto_id']) and not len(filtros_json['status_id']) and not len(filtros_json['fecha_inicio']) and not len(filtros_json['fecha_final']):
			recientes = True

		if 'contacto_id' in filtros_json and len(filtros_json['contacto_id']):
			contacto_id = filtros_json['contacto_id']
			contacto = Contacto.objects.get(id=contacto_id)
			dest_list = sr.getDestinatarios(request,contacto_id)

		if len(filtros_json['compania_id']):
			compania_id = filtros_json['compania_id']
			compania = Compania.objects.get(id=compania_id)	
	else:
		recientes = True

	investigaciones = get_investigaciones_list(filtros_json)

	for i in investigaciones:
		i.ciudad = i.candidato.direccion_set.all()[0].ciudad
		i.entrevista = i.entrevistapersona_set.all()[0].entrevistainvestigacion_set.all()[0] if i.entrevistapersona_set.all().count() else None
		i.trayectoria = i.candidato.trayectorialaboral_set.filter(visible_en_status=True, status=True)
		for t in i.trayectoria:
			t.cardex = t.evaluacion_set.all()[0].opinion_set.filter(categoria=2)[0].opinion if t.evaluacion_set.all()[0].opinion_set.filter(categoria=2).count() else None
			
	return render_to_response('sections/reportes/panel.html', locals())

@csrf_exempt
def exportar_pdf(request):
	filtros_json = request.session.get('filtros_search_reportes', None)
	investigaciones = get_investigaciones_list(filtros_json)

	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="reporte_investigaciones_cliente.pdf"'

	# Create the PDF object, using the response object as its "file."
	p = canvas.Canvas(response)

	# Draw things on the PDF. Here's where the PDF generation happens.
	# See the ReportLab documentation for the full list of functionality.
	
	content = ''
	c = 1
	for i in investigaciones:
		content = unicode(i.compania.nombre)+' / '+unicode(i.candidato.nombre)+' / '+unicode(i.puesto)
		p.drawString(80, 750-c, content)
		c=c+15

	# Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	return response

@csrf_exempt
def search_reportes(request):
	response = { 'status' : False}
	if request.method == 'POST' and request.is_ajax():
		
		compania_id = request.POST.get('compania_id', '')
		compania_nombre = request.POST.get('compania_nombre', '')
		contacto_id = request.POST.get('contacto_id', '')
		status_id = request.POST.get('status_id', '')
		fecha_inicio = request.POST.get('fecha_inicio', '')
		fecha_final = request.POST.get('fecha_final', '')
		
		request.session['filtros_search_reportes'] = {'compania_id':compania_id, 'compania_nombre':compania_nombre, 'contacto_id':contacto_id, 'status_id':status_id, 'fecha_inicio':fecha_inicio,'fecha_final':fecha_final}
		 
		response = { 'status' : True}

	return HttpResponse(json.dumps(response), content_type='application/json')

@csrf_exempt
def reset_filtros(request):
	request.session['filtros_search_reportes'] = None
	response = { 'status' : True}
	return HttpResponse(json.dumps(response), content_type='application/json')

def get_investigaciones_list(filtros_json):
	investigaciones = Investigacion.objects.filter(status_active=True).order_by('fecha_recibido')

	if filtros_json != None:
		if not len(filtros_json['compania_id']) and not len(filtros_json['compania_nombre']) and not len(filtros_json['contacto_id']) and not len(filtros_json['status_id']) and not len(filtros_json['fecha_inicio']) and not len(filtros_json['fecha_final']):
			recientes = True
			investigaciones = investigaciones.order_by('fecha_recibido')[:20]

		else:
			if len(filtros_json['compania_id']):
				investigaciones = investigaciones.filter(compania__id=filtros_json['compania_id'])

			if 'contacto_id' in filtros_json and len(filtros_json['contacto_id']):
				investigaciones = investigaciones.filter(contacto__id=filtros_json['contacto_id'])

			if len(filtros_json['status_id']):
				investigaciones = investigaciones.filter(status_general=filtros_json['status_id'])

			if len(filtros_json['fecha_inicio']) and len(filtros_json['fecha_final']):
				fecha_inicio_format = datetime.datetime.strptime(filtros_json['fecha_inicio'], '%d/%m/%y').strftime('%Y-%m-%d')
				fecha_final_format = datetime.datetime.strptime(filtros_json['fecha_final'], '%d/%m/%y').strftime('%Y-%m-%d')
				investigaciones = investigaciones.filter(fecha_recibido__range=(fecha_inicio_format, fecha_final_format))

	else:
		recientes = True
		investigaciones = investigaciones.order_by('fecha_recibido')[:20]

	return investigaciones