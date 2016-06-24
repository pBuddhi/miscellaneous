# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-21 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dummyapp', '0020_auto_20160618_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='room',
        ),
        migrations.AddField(
            model_name='accommodation',
            name='accommodation_type',
            field=models.CharField(default='hotel', max_length=250),
        ),
        migrations.AddField(
            model_name='package',
            name='accommodation',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='dummyapp.Accommodation'),
            preserve_default=False,
        ),
    ]
