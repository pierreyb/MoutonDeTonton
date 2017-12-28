# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-11 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Lutte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_male', models.CharField(max_length=50)),
                ('alive_number', models.IntegerField(blank=True)),
                ('dead_number', models.IntegerField(blank=True)),
                ('birth_weight_1', models.CharField(blank=True, max_length=50)),
                ('birth_weight_2', models.CharField(blank=True, max_length=50)),
                ('birth_weight_3', models.CharField(blank=True, max_length=50)),
                ('bred_number', models.IntegerField(blank=True)),
                ('sex', models.CharField(blank=True, max_length=50)),
                ('remark', models.TextField(blank=True)),
                ('lutte_type', models.CharField(default='1', max_length=5)),
                ('code', models.CharField(blank=True, max_length=5)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Mouton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sanitel_number', models.CharField(max_length=16, unique=True)),
                ('herbook_number', models.CharField(blank=True, max_length=16)),
                ('birth_date', models.DateField(blank=True)),
                ('sex', models.CharField(choices=[('F', 'F')], max_length=1)),
                ('out_date', models.DateField(blank=True)),
                ('out_text', models.CharField(blank=True, max_length=5)),
                ('in_text', models.CharField(blank=True, max_length=5)),
                ('race', models.CharField(blank=True, choices=[('BLEU DU MAINE', 'BLEU DU MAINE')], max_length=50)),
                ('traitement', models.TextField(blank=True)),
                ('comment', models.TextField(blank=True)),
                ('birth_siblings', models.CharField(blank=True, choices=[('Simple', 'Simple')], max_length=50)),
                ('father', models.CharField(blank=True, max_length=50)),
                ('mother', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('birth_weight', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('one_month_weight', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('one_month_date', models.DateField(blank=True)),
                ('two_month_weight', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('two_month_date', models.DateField(blank=True)),
                ('third_weight', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('third_date', models.DateField(blank=True)),
                ('fourth_weight', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('fourth_date', models.DateField(blank=True)),
                ('sold_weight', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('slaughtered_weight', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('mouton_class', models.CharField(blank=True, max_length=50)),
                ('sold_value', models.DecimalField(blank=True, decimal_places=3, max_digits=18)),
                ('origin_number', models.CharField(blank=True, max_length=10)),
                ('destination_number', models.CharField(blank=True, max_length=12)),
                ('qualification', models.CharField(blank=True, max_length=50)),
                ('genotype', models.CharField(blank=True, max_length=15)),
                ('birth', models.CharField(blank=True, max_length=15)),
                ('blood_test', models.TextField(blank=True)),
                ('lot_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='moutons.Lot')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('mouton_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moutons.Mouton')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.AddField(
            model_name='lutte',
            name='male_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='moutons.Mouton'),
        ),
        migrations.AddField(
            model_name='lutte',
            name='mouton_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moutons.Mouton'),
        ),
    ]