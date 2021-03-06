# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-08 20:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moutons', '0016_auto_20171107_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouton',
            name='herbook_number',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='n° Herbook'),
        ),
        migrations.AlterField(
            model_name='mouton',
            name='sanitel_number',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator('^\\d{4,5}(\\-\\-)?\\d{4}$', 'Sanitel doit avoir 8 ou 9 chiffres')], verbose_name='n° sanitel'),
        ),
    ]
