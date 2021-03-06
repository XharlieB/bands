# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 02:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreSeccion', models.CharField(max_length=6)),
                ('numeroAsientosSeccion', models.IntegerField(blank=True, max_length=8)),
                ('costoSeccion', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='venue',
            name='asientos',
        ),
        migrations.AddField(
            model_name='venue',
            name='numeroAsientos',
            field=models.IntegerField(blank=True, default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venue',
            name='secciones',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='seccion', to='eventos.Seccion'),
        ),
    ]
