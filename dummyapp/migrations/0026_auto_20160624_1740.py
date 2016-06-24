# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummyapp', '0025_airportcodesimport'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagequote',
            name='price',
            field=models.CharField(default='5000', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='packagequote',
            name='price_with_coupon',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
