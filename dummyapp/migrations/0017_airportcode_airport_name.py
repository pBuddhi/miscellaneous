# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-11 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummyapp', '0016_auto_20160611_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='airportcode',
            name='airport_name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
