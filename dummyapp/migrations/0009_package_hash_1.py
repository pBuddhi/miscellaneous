# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummyapp', '0008_auto_20160602_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='hash_1',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
