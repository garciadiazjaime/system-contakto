# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-19 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobranza', '0002_factura'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='nombre',
            field=models.CharField(blank=True, default=b'', max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='factura',
            name='rfc',
            field=models.CharField(blank=True, default=b'', max_length=50, null=True),
        ),
    ]
