# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-19 01:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20170319_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
