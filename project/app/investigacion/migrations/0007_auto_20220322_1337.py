# Generated by Django 2.2.24 on 2022-03-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigacion', '0006_gestorinvestigacion_estatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestorinvestigacion',
            name='fecha_asignacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gestorinvestigacion',
            name='fecha_atencion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gestorinvestigacion',
            name='fecha_registro',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]