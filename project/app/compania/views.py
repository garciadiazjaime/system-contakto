# -*- coding: utf-8 -*-

from django.shortcuts import HttpResponse, render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from app.investigacion.models import Investigacion
from app.bitacora.models import Bitacora
from app.compania.models import Compania, Contacto
from app.compania.forms import CompaniaForm, ContactoForm
from django.db.models import Q
import json


@login_required(login_url='/login', redirect_field_name=None)
@user_passes_test(lambda u: u.is_staff, login_url='/', redirect_field_name=None)
def panel(request):
	es_chrome = 'Chrome' in request.META['HTTP_USER_AGENT'] #Fix por pixeles en Chrome (input-group-addon de bootstrap)
	page = 'empresas'
	empresas = Compania.objects.filter(status=True).order_by('nombre')

	#Para search sidebar
	filtros_json = request.session.get('filtros_search_empresa', None)
	if filtros_json != None:
		if len(filtros_json['compania_nombre']):
			empresas = empresas.filter(nombre__contains=filtros_json['compania_nombre'])
		if len(filtros_json['es_cliente']):
			empresas = empresas.filter(es_cliente=True)
	
	return render_to_response('sections/empresa/panel.html', locals())

@login_required(login_url='/login', redirect_field_name=None)
@user_passes_test(lambda u: u.is_staff, login_url='/', redirect_field_name=None)
def nueva(request, investigacion_id=''):
	page = 'empresas'
	title = 'Crear nueva empresa'
	boton_captura_contactos = True

	boton_cancelar_url = '/candidato/investigacion/'+str(investigacion_id)+'/trayectoria/nueva' if investigacion_id else '/empresas'

	if request.POST:
		form = CompaniaForm(request.POST)
		if form.is_valid():
			emp_nueva = form.save()
			b = Bitacora(action='empresas-creada: ' + unicode(request.POST.get('name')), user=request.user)
			b.save()
			if investigacion_id:
				if 'guargar_capt_contactos' in request.POST:
					return HttpResponseRedirect('/empresa/'+str(emp_nueva.id)+'/contacto/nuevo/ref/'+str(investigacion_id))
				else:
					return HttpResponseRedirect('/candidato/investigacion/'+str(investigacion_id)+'/trayectoria/nueva/empresa/'+str(emp_nueva.id))
				
			elif 'guargar_capt_contactos' in request.POST:
				return HttpResponseRedirect('/empresa/'+str(emp_nueva.id)+'/contacto/nuevo')
			else:
				return HttpResponseRedirect('/empresas/exito')
	else:
		form = CompaniaForm()
	return render_to_response('sections/empresa/form.html', locals(), context_instance=RequestContext(request))


@login_required(login_url='/login', redirect_field_name=None)
@user_passes_test(lambda u: u.is_staff, login_url='/', redirect_field_name=None)
def editar(request, compania_id, investigacion_id='', trayectoria_id=''):
	company = Compania.objects.filter(id=compania_id)
	page = 'empresas'
	title = 'Editar empresa: ' + str(company[0])

	boton_cancelar_url = '/candidato/investigacion/'+str(investigacion_id)+'/editar/trayectoria/'+str(trayectoria_id) if investigacion_id and trayectoria_id else '/empresas'

	# variable to determin if we can add this company to a client
	enable_move_to_client = True
	
	# variable to determin if we can delete company, it helps to show 'delete' btn
	delete_company_enable = True
	if request.POST:
		form = CompaniaForm(request.POST, instance=company[0])
		if form.is_valid():
			form.save()
			b = Bitacora(action='empresas-editada: ' + unicode(request.POST.get('name')), user=request.user)
			b.save()
			if investigacion_id:
				return HttpResponseRedirect('/candidato/investigacion/'+str(investigacion_id)+'/editar/trayectoria/'+str(trayectoria_id)+'/exito')
			else:
				return HttpResponseRedirect('/empresas/exito')
	else:
		form = CompaniaForm(instance=company[0])
	return render_to_response('sections/empresa/form.html', locals(), context_instance=RequestContext(request))
	
@login_required(login_url='/login', redirect_field_name=None)
@user_passes_test(lambda u: u.is_staff, login_url='/', redirect_field_name=None)
def borrar(request, compania_id):
	company = Compania.objects.get(id=compania_id)
	company.status = False
	company.save()
	b = Bitacora(action='borrar-empresa: ' + unicode(company), user=request.user)
	b.save()
	return HttpResponseRedirect('/empresas/exito')


'''
	Contactos
'''
@login_required(login_url='/login', redirect_field_name=None)
@user_passes_test(lambda u: u.is_staff, login_url='/', redirect_field_name=None)
def contactos(request, compania_id):
	company = Compania.objects.get(id=compania_id)
	contactos = Contacto.objects.filter(compania=company,status=True).order_by('-id')
	page = 'empresas'
	title = 'Contactos empresa: ' + unicode(company.nombre)
	
	empresas = Compania.objects.filter(status=True).order_by('nombre')

	#Para search sidebar
	filtros_json = request.session.get('filtros_search_empresa', None)
	if filtros_json != None:
		if len(filtros_json['compania_nombre']):
			empresas = empresas.filter(nombre__contains=filtros_json['compania_nombre'])
		if len(filtros_json['es_cliente']):
			empresas = empresas.filter(es_cliente=True)

	return render_to_response('sections/empresa/contacto/panel.html', locals(), context_instance=RequestContext(request))

@login_required(login_url='/login', redirect_field_name=None)
def contacto_nuevo(request, compania_id='', investigacion_id=''):
	company = Compania.objects.get(id=compania_id)

	page = 'empresas'
	title = 'Crear nuevo contacto de '+unicode(company.nombre)

	boton_capturar_otro = True
	boton_cancelar_url = '/candidato/investigacion/'+str(investigacion_id)+'/trayectoria/nueva/empresa/'+str(compania_id) if investigacion_id else '/empresa/'+str(compania_id)+'/contactos'
	pwd_label_text = 'Capturar para crear un usuario de este contacto'

	if request.POST:
		email = request.POST.get('email', '')
		users_with_email_count = User.objects.filter(email=email).count() if len(email) else 0

		form = ContactoForm(request.POST)
		if form.is_valid() and not users_with_email_count:
			nuevo_contacto = form.save(commit=False)
			nuevo_contacto.compania = company
			nuevo_contacto.save()

			#crear usuario contacto en caso de haber capturado 'password'
			p = request.POST.get('password', '')
			if len(p):
				new_user = User(email=nuevo_contacto.email)
				new_user.set_password(p)
				new_user.save()
				new_user.username = "contacto_"+str(new_user.id)
				new_user.groups.add(Group.objects.get(name='contactos'))
				new_user.save()

			b = Bitacora(action='contacto-creado: ' + request.POST.get('nombre') +' / '+ unicode(company.nombre), user=request.user)
			b.save()

			#Si se tiene el investigacion_id como referencia, se redirecciona
			if investigacion_id:
				if 'guargar_capturar_otro' in request.POST:
					return HttpResponseRedirect('/empresa/'+str(company.id)+'/contacto/nuevo/ref/'+str(investigacion_id)+'/exito')
				else:
					return HttpResponseRedirect('/candidato/investigacion/'+str(investigacion_id)+'/trayectoria/nueva/empresa/'+str(company.id))

			elif 'guargar_capturar_otro' in request.POST:
				return HttpResponseRedirect('/empresa/'+str(company.id)+'/contacto/nuevo/exito')
			else:
				return HttpResponseRedirect('/empresa/'+str(company.id)+'/contactos/exito')
		elif users_with_email_count:
			error_msg = 'Este email ya está registrado.'

	else:
		form = ContactoForm()
	return render_to_response('sections/empresa/contacto/form.html', locals(), context_instance=RequestContext(request))

@login_required(login_url='/login', redirect_field_name=None)
@user_passes_test(lambda u: u.is_staff, login_url='/', redirect_field_name=None)
def contacto_editar(request, compania_id, contacto_id):
	company = Compania.objects.get(id=compania_id)
	contacto = Contacto.objects.get(id=contacto_id)
	boton_capturar_otro = False
	# variable to determin if we can delete company, it helps to show 'delete' btn
	delete_contact_enable = True

	page = 'empresas'
	title = 'Editar contacto: ' + unicode(contacto.nombre) + ' / ' + unicode(company.nombre)
	
	boton_cancelar_url = '/empresa/'+str(compania_id)+'/contactos'

	#admin
	#Variable con el usuario correspondiente al contacto en caso de que exista, de lo contraro es False
	usuario_contacto = User.objects.filter(email=contacto.email)[0] if (User.objects.filter(email=contacto.email).count()) else False
	pwd_label_text = 'Capturar solo si se desea cambiar su contraseña' if usuario_contacto else 'Capturar para crear un usuario de este contacto'

	if request.POST:
		og_email = contacto.email
		new_email = request.POST.get('email', '')

		#Variable que indica si existe algun usuario registrado con el email de la forma ( >= 1 ), solo en caso de ser un email diferente al del usuario actual
		users_with_email_count = User.objects.filter(email=new_email).count() if (len(new_email) and new_email != og_email) else 0
		
		form = ContactoForm(request.POST, instance=contacto)
		if form.is_valid() and not users_with_email_count:
			contacto_instance = form.save()

			### Operaciones sobre usuario contacto (crear/editar)
			p = request.POST.get('password', '')
			#Si existe usuario del contacto, actualizar password/email
			if usuario_contacto and (len(p) or new_email != og_email):
				if len(p):
					usuario_contacto.set_password(p)
				#Si el email capturado es diferente, actualizar el usuario
				if (new_email != og_email):
					usuario_contacto.email = new_email
				usuario_contacto.save()
			#De lo contrario, en caso de haber capturado pwd 'len(p)', crear usuario del contacto
			elif len(p):
				new_user = User(email=new_email)
				new_user.set_password(p)
				new_user.username = new_email
				new_user.save()

				new_user.groups.add(Group.objects.get(name='contactos'))
				new_user.save()

			### Actualizar costos de investigaciones de contacto que tengan asignado un tipo de inv, pero no un costo.
			for status in range(1,3):
				data = Investigacion.objects.filter(contacto=contacto, tipo_investigacion_status=status)#.filter(cobranza__monto=None, cobranza__folio='')
				if data.count():
					for inv in data:
						f = inv.cobranza_set.all()[0]
						if not f.monto and not f.folio:
							f.monto = contacto_instance.costo_inv_laboral if status == 1 else contacto_instance.costo_inv_completa
							f.save()
			b = Bitacora(action='contacto-editado: ' + unicode(request.POST.get('nombre')) +' / ' + unicode(company.nombre), user=request.user)
			b.save()
			return HttpResponseRedirect('/empresa/'+str(company.id)+'/contactos/exito')
		
		elif users_with_email_count:
			error_msg = 'Este email ya está registrado.'
	else:
		form = ContactoForm(instance=contacto)
	return render_to_response('sections/empresa/contacto/form.html', locals(), context_instance=RequestContext(request))

@login_required(login_url='/login', redirect_field_name=None)
@user_passes_test(lambda u: u.is_staff, login_url='/', redirect_field_name=None)
def contacto_borrar(request, compania_id, contacto_id):
	company = Compania.objects.get(id=compania_id)
	contacto = Contacto.objects.get(id=contacto_id)
	contacto.nombre = contacto.nombre + ' (-)'
	contacto.status = False
	contacto.save()
	b = Bitacora(action='borrar-contacto: ' + unicode(contacto) + ' / ' + unicode(company.nombre), user=request.user)
	b.save()
	return HttpResponseRedirect('/empresa/' + str(company.id) + '/contactos/exito')

'''
	Ajax
'''

@login_required(login_url='/login', redirect_field_name=None)
def get_contactos(request, compania_id, investigacion_id=''):
	contacto_investigacion_id = Investigacion.objects.get(id=investigacion_id).contacto.id if investigacion_id else ''
	compania = Compania.objects.filter(id=compania_id)
	response = {'status': False}
	if request.method == 'GET' and request.is_ajax() or True:
		if len(compania):
			contactos = Contacto.objects.filter(Q(compania=compania[0], status=True)|Q(compania=compania[0], id=contacto_investigacion_id)).order_by('nombre') if contacto_investigacion_id else Contacto.objects.filter(Q(compania=compania[0], status=True)).order_by('nombre')
			data = []
			for c in contactos:
				data.append({
					'id': c.id,
					'nombre': c.nombre
					})
			response = {'status': True, 'contactos': data}
	return HttpResponse(json.dumps(response), mimetype='application/json')

@csrf_exempt
def search_empresas(request):
	response = { 'status' : False}
	if request.method == 'POST' and request.is_ajax():
		compania_nombre = request.POST.get('compania_nombre', '')
		es_cliente = request.POST.get('es_cliente', '')
		request.session['filtros_search_empresa'] = {'compania_nombre':compania_nombre, 'es_cliente':es_cliente}	
		response = { 'status' : True}
	return HttpResponse(json.dumps(response), content_type='application/json')

@csrf_exempt
def reset_filtros(request):
	request.session['filtros_search_empresa'] = None
	response = { 'status' : True}
	return HttpResponse(json.dumps(response), content_type='application/json')