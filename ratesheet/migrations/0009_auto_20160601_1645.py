# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratesheet', '0008_auto_20160601_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomrate',
            name='sailing_dates',
            field=models.ManyToManyField(null=True, to='ratesheet.SailingDate'),
        ),
    ]
