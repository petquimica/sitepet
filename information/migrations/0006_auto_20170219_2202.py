# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0005_auto_20170212_0217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='information',
        ),
        migrations.RemoveField(
            model_name='link',
            name='information',
        ),
        migrations.AddField(
            model_name='information',
            name='link',
            field=models.URLField(default=1, help_text='Link para o Google Driver', verbose_name='Link'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Link',
        ),
    ]
