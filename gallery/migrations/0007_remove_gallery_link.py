# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 22:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_gallery_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='link',
        ),
    ]
