# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-21 21:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moutons', '0024_auto_20180120_2235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lutte',
            options={'ordering': ('-date_lutte',)},
        ),
    ]