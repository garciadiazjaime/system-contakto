# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-10-05 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobranza', '0003_auto_20200619_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cobranza',
            name='folio',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cobranza',
            name='status_cobranza',
            field=models.CharField(blank=True, choices=[('0', 'Status 1'), ('1', 'Status 2'), ('2', 'Pagada')], default='0', max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='nombre',
            field=models.CharField(blank=True, default='', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='rfc',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
