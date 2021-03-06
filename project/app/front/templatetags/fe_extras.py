# -*- coding: utf-8 -*-
from django import template
from django.template import Context, loader, RequestContext
from app.cobranza.models import Cobranza
from app.investigacion.models import Investigacion
from app.entrevista.models import EntrevistaInvestigacion, EntrevistaGradoEscolaridad
from app.persona.models import TrayectoriaLaboral
import logging, re, os

register = template.Library()
	
@register.filter(name = 'tipo_investigacion_status')
def tipo_investigacion_status(value):
	status = ''
	for status in Investigacion.TIPO_INVESTIGACION_OPCIONES:
		if status[0] == value:
			return status[1]
	
	return ''
	
@register.filter(name = 'investigacion_status')
def investigacion_status(value):
	status = ''
	try:
		status = Investigacion.STATUS_OPCIONES[int(value)][1]
	except Exception as e:
		print (e)
	return status if len(status) else '---'

@register.filter(name = 'investigacion_status_gral')
def investigacion_status_gral(value):
	status = ''
	try:
		status = Investigacion.STATUS_GRAL_OPCIONES[int(value)][1]
	except Exception as e:
		print (e)
	return status if len(status) else '---'
	
@register.filter(name = 'investigacion_resultado')
def investigacion_resultado(value):
	status = ''
	if not value:
		return ''

	try:
		status = int(value)
	except Exception as e:
		pass

	status = Investigacion.RESULTADO_OPCIONES[status][1]

	return status
	
@register.filter(name = 'entrevista_grado_academico')
def entrevista_grado_academico(value):
	grados_list = EntrevistaGradoEscolaridad.GRADO_OPCIONES
	for g in grados_list:
		if g[0] == value:
			return g[1]
	return '---'

@register.filter(name = 'entrevista_status_autorizada')
def entrevista_status_autorizada(value):
	index = ''
	try:
		index = 'Sí' if int(value) == 1 else 'No'
	except Exception as e:
		print (e)
	return index

@register.filter(name = 'motivo_salida')
def motivo_salida(value):
	status = ''
	try:
		status = TrayectoriaLaboral.SALIDA_OPCIONES[int(value)][1]
	except Exception as e:
		print (e)
	return status if len(status) else '---'

@register.filter
def filename(value):
    """Get basename of full-path. Return error if file not found."""
    return os.path.basename(value)

@register.filter(name = 'clean_type')
def clean_type(value):
	doc_list = (
				('acta_nacimiento','ACTA DE NACIMIENTO'),
				('acta_matrimonio','ACTA DE MATRIMONIO'),
				('comprobante_domicilio','COMPROBANTE DE DOMICILIO'),
				('id_oficial','COMPROBANTE DE IDENTIFICACIÓN'),
				('comprobante_nss','COMPROBANTE DE NSS'),
				('curp','CURP'),
				('cartilla_smn','CARTILLA SMN'),
				('ultimo_grado_estudio','ÚLTIMO GRADO DE ESTUDIOS:'),
				('cartas_laborales','CARTAS LABORALES'),
				('motivos_falta_docs','EN CASO DE QUE NO, ESPECIFICAR DOCUMENTO Y RAZÓN POR QUE NO LA PRESENTO'),
				('orden','ORDEN'),
				('limpieza','LIMPIEZA'),
				('conservacion','CONSERVACIÓN'),
				('disponibilidad','DISPONIBILIDAD'),
				('puntualidad','PUNTUALIDAD'),
				('apariencia_fisica','APARIENCIA FÍSICA'),
				('colaboracion','COLABORACIÓN'),
				('actitud','ACTITUD'),
				('trabajo','Ha trabajado anteriormente en la empresa'),
				('familiar','Tiene algún familiar trabajando en la empresa'),
				('investigado','Investigado'), 
				('conyuge','Cónyuge'), 
				('padres','Padres'), 
				('hermanos','Hermanos'), 
				('otros','Otros'), 
				('total','Total'), 
				('impuestos','Impuestos'), 
				('vestimenta','Vestimenta'), 
				('gastos_automovil','Gastos automóvil'), 
				('transporte_publico','Transporte publico'), 
				('alimentacion','Alimentación'), 
				('educacion','Educación'), 
				('medico','Médico'), 
				('diversos','Diversión'), 
				('servicios','Servicios (Luz, Agua, Teléfono)'), 
				('serv_domestico','Serv. doméstico'), 
				('seguros','Seguros'), 
				('deuda1','Deuda 1'), 
				('deuda2','Deuda 2'), 
				('otros','Otros'), 
				('total','Total'),
			)

	for d in doc_list:
		if d[0] == value:
			return d[1]
	return value

@register.filter(name = 'verbose_name')
def verbose_name(instance, field_name):
	return instance._meta.get_field(field_name).verbose_name.title()


@register.filter(name = 'get_investigacion_cost')
def get_investigacion_cost(investigacion_raw):
	if investigacion_raw[14] == 1 and investigacion_raw[19]:
		return "$ " + str(investigacion_raw[19])
	elif investigacion_raw[14] == 2 and investigacion_raw[20]:
		return "$ " + str(investigacion_raw[20])
							
	return 'REQUERIDO'
