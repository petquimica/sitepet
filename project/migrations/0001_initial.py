# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('content', models.TextField(max_length=1000, verbose_name='Conteúdo')),
                ('link', models.URLField(blank=True, help_text='Link para o Google Driver', verbose_name='Google Driver')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
                'ordering': ['-created_at'],
            },
        ),
    ]
