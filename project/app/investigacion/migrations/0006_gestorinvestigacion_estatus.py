# Generated by Django 2.2.24 on 2022-03-16 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigacion', '0005_gestorinvestigacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestorinvestigacion',
            name='estatus',
            field=models.PositiveSmallIntegerField(choices=[(1, 'ASIGNADA'), (2, 'EN ATENCIÓN'), (3, 'CONCLUIDA')], default=1),
        ),
    ]