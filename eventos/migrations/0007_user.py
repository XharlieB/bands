# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0006_artista_monedacambio'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('nombreUser', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]
