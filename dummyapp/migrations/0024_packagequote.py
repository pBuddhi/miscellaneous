# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummyapp', '0023_package_transfer_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('pkg_hash', models.CharField(max_length=250)),
                ('coupon_code', models.CharField(blank=True, max_length=250)),
            ],
        ),
    ]
