# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-17 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moutons', '0010_auto_20170617_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouton',
            name='birth_date',
            field=models.DateField(help_text='dd/mm/yyyy'),
        ),
    ]
