# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-10 21:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dummyapp', '0015_airportcode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AirportCodes',
        ),
        migrations.DeleteModel(
            name='AirportCodesNew',
        ),
    ]