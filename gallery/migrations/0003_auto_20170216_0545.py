# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20170216_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='favorite',
            field=models.BooleanField(default=False, help_text='Escolher a foto principal da galeria para colocar como destaque na página principal', verbose_name='Favorita'),
        ),
    ]
