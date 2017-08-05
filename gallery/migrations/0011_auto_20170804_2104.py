# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-04 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_auto_20170804_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='images',
        ),
        migrations.AddField(
            model_name='image',
            name='gallery',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gallery.Gallery'),
            preserve_default=False,
        ),
    ]
