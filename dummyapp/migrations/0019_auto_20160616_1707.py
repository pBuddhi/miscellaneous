# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-16 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummyapp', '0018_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='hotel',
            field=models.TextField(max_length=250),
        ),
    ]
