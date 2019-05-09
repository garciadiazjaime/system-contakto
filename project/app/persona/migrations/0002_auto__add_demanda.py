# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Demanda'
        db.create_table('persona_demanda', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['persona.Persona'])),
            ('tiene_demanda', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('empresa', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('motivo', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('audiencias', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('conclusion', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal('persona', ['Demanda'])


    def backwards(self, orm):
        # Deleting model 'Demanda'
        db.delete_table('persona_demanda')


    models = {
        'compania.compania': {
            'Meta': {'object_name': 'Compania'},
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'es_cliente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'notas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'razon_social': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'referencia_correo': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'rfc_direccion': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sucursal': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'telefono_alt': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'persona.academica': {
            'Meta': {'object_name': 'Academica'},
            'cedula_prof_ano_exp': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cedula_profesional': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'estudios_actuales': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"})
        },
        'persona.actividadeshabitos': {
            'Meta': {'object_name': 'ActividadesHabitos'},
            'extras': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'frecuencia_alcohol': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'frecuencia_otras_sust': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'frecuencia_tabaco': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'tiempo_libre': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        'persona.aspectocandidato': {
            'Meta': {'object_name': 'AspectoCandidato'},
            'estatus': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'persona.aspectohogar': {
            'Meta': {'object_name': 'AspectoHogar'},
            'estatus': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'persona.automovil': {
            'Meta': {'object_name': 'Automovil'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liquidacion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'marca': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'modelo_ano': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'valor_comercial': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        'persona.bienesraices': {
            'Meta': {'object_name': 'BienesRaices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liquidacion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'tipo_inmueble': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'valor_comercial': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        'persona.caractaristicasvivienda': {
            'Meta': {'object_name': 'CaractaristicasVivienda'},
            'hipotecada': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otra': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'prestada': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'propia': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'renta_mensual': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rentada': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'valor_aproximado': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'persona.cuadroevaluacion': {
            'Meta': {'object_name': 'CuadroEvaluacion'},
            'conclusiones': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_viable': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'reservas': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'viable': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        'persona.cuentadebito': {
            'Meta': {'object_name': 'CuentaDebito'},
            'ahorro': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'antiguedad': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'saldo_mensual': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        'persona.demanda': {
            'Meta': {'object_name': 'Demanda'},
            'audiencias': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'conclusion': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'tiene_demanda': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        'persona.deudaactual': {
            'Meta': {'object_name': 'DeudaActual'},
            'cantidad_total': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'fecha_otorgamiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'pago_mensual': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'saldo_actual': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        'persona.direccion': {
            'Meta': {'object_name': 'Direccion'},
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'cp': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'default': "'Baja California'", 'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"})
        },
        'persona.distribuciondimensiones': {
            'Meta': {'object_name': 'DistribucionDimensiones'},
            'banos': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cocheras': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cocina': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'comedor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'habitaciones': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patios': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'salas': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'persona.documentocotejado': {
            'Meta': {'object_name': 'DocumentoCotejado'},
            'estatus': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'persona.economica': {
            'Meta': {'object_name': 'Economica'},
            'concepto': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.FloatField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'persona.evaluacion': {
            'Meta': {'object_name': 'Evaluacion'},
            'adaptabilidad': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'asistencia': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'compromiso': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'disponibilidad': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'honestidad': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivacion': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'productividad': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'puntualidad': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'relacion_companeros': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'relacion_jefe_inmediato': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'responsabilidad': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'solucion_problemas': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'toma_decisiones': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'trayectoriaLaboral': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.TrayectoriaLaboral']"})
        },
        'persona.file': {
            'Meta': {'object_name': 'File'},
            'fecha_registro': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'persona.gradoescolaridad': {
            'Meta': {'object_name': 'GradoEscolaridad'},
            'anos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'certificado': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'grado': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"})
        },
        'persona.infopersonal': {
            'Meta': {'object_name': 'InfoPersonal'},
            'cualidades': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'defectos': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objetivo_en_empresa': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'objetivo_personal': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'tatuajes': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'trabajo_que_desarrolla': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'persona.informante': {
            'Meta': {'object_name': 'Informante'},
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Evaluacion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'puesto': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'})
        },
        'persona.legalidad': {
            'Meta': {'object_name': 'Legalidad'},
            'afiliado_sindicato': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'antecedentes_penales': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'demandas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'sindicato': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        'persona.licencia': {
            'Meta': {'object_name': 'Licencia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '14'})
        },
        'persona.miembromarcofamiliar': {
            'Meta': {'object_name': 'MiembroMarcoFamiliar'},
            'edad': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'residencia': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'persona.opinion': {
            'Meta': {'object_name': 'Opinion'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Evaluacion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opinion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'persona.origen': {
            'Meta': {'object_name': 'Origen'},
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'nacionalidad': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"})
        },
        'persona.otroidioma': {
            'Meta': {'object_name': 'OtroIdioma'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idioma': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'porcentaje': ('django.db.models.fields.IntegerField', [], {})
        },
        'persona.persona': {
            'Meta': {'object_name': 'Persona'},
            'curp': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'edad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'estado_civil': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'estatus': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fecha_matrimonio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_registro': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ife': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'malos_terminos': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'medio_utilizado': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'nss': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'pasaporte': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'smn': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'tiempo_radicando': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'})
        },
        'persona.prestacionvivienda': {
            'Meta': {'object_name': 'PrestacionVivienda'},
            'activo': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'categoria_viv': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'fecha_tramite': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_credito': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'uso': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        'persona.propietariovivienda': {
            'Meta': {'object_name': 'PropietarioVivienda'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parentesco': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"})
        },
        'persona.referencia': {
            'Meta': {'object_name': 'Referencia'},
            'domicilio': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugares_labor_evaluado': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'opinion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parentesco': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'tiempo_conocido': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        'persona.salud': {
            'Meta': {'object_name': 'Salud'},
            'accidentes': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ejercicio_tipo_frecuencia': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'embarazo_meses': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'enfermedades_familiares': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'enfermedades_mayor_frecuencia': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'estatura_mts': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion_medica': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'intervenciones_quirurgicas': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'peso_kg': ('django.db.models.fields.FloatField', [], {}),
            'salud_fisica': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'salud_visual': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tratamiento_medico_psicologico': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'persona.seguro': {
            'Meta': {'object_name': 'Seguro'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'registro_completo': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ultimas_aportaciones': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'verificado_enburo': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'persona.situacionvivienda': {
            'Meta': {'object_name': 'SituacionVivienda'},
            'conservacion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'personas_viven_con_evaluado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sector_socioeconomico': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tamano_aprox_mts2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tiempo_radicando': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo_mobiliario': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'persona.tarjetacreditocomercial': {
            'Meta': {'object_name': 'TarjetaCreditoComercial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'limite_credito': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'pago_minimo': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'saldo_actual': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        'persona.telefono': {
            'Meta': {'object_name': 'Telefono'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'parentesco': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"})
        },
        'persona.tipoinmueble': {
            'Meta': {'object_name': 'TipoInmueble'},
            'casa': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'departamento': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'terreno_compartido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'vivienda_popular': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'persona.trayectorialaboral': {
            'Meta': {'object_name': 'TrayectoriaLaboral'},
            'afiliado_sindicato': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'aparece_nss': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'aportaciones_fecha_final': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'aportaciones_fecha_inicial': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'carta_laboral': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'carta_laboral_expide': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'compania': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compania.Compania']"}),
            'cumplio_objetivos': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'funciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jefe_inmediato': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'jefe_inmediato_puesto': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'manejo_valores': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'motivo_salida': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'no_personas_cargo': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'observaciones_generales': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'periodo_alta': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'periodo_baja': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['persona.Persona']"}),
            'puesto_final': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'puesto_inicial': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'recontratable': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'reporta_candidato': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sueldo_final': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'sueldo_inicial': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'terminada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'visible_en_status': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['persona']