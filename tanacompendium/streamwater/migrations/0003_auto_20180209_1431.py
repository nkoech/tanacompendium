# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-09 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streamwater', '0002_waterquality_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waterquality',
            old_name='turbidity_NTU',
            new_name='turbidity_ntu',
        ),
    ]