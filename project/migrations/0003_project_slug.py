# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20170220_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=1, max_length=100, verbose_name='Identificador'),
            preserve_default=False,
        ),
    ]
