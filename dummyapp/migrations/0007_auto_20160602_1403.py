# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummyapp', '0006_package_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='slug',
            field=models.SlugField(),
        ),
    ]
