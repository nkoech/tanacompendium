# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-09 12:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streamwater', '0003_auto_20180209_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waterquality',
            name='slug',
        ),
    ]
