# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('document', models.FileField(blank=True, null=True, upload_to='documents/information', verbose_name='Documentos')),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('content', models.TextField(max_length=1000, verbose_name='Conteúdo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Informação',
                'verbose_name_plural': 'Informações',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('link', models.URLField(verbose_name='Link')),
                ('information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='information.Information', verbose_name='Informação')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='information',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='information.Information', verbose_name='Informação'),
        ),
    ]
