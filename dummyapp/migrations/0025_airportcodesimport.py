# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummyapp', '0024_packagequote'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirportCodesImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=250)),
                ('airport_code', models.CharField(max_length=250)),
                ('airport_name', models.CharField(max_length=250)),
                ('country_name', models.CharField(max_length=250)),
                ('country_abbrev', models.CharField(max_length=250)),
                ('world_area_code', models.CharField(max_length=250)),
            ],
        ),
    ]