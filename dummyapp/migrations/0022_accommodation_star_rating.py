# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-21 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummyapp', '0021_auto_20160621_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodation',
            name='star_rating',
            field=models.CharField(default=5, max_length=250),
        ),
    ]
