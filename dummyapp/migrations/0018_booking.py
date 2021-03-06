# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-16 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummyapp', '0017_airportcode_airport_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name_1', models.CharField(max_length=250)),
                ('guest_name_2', models.CharField(max_length=250)),
                ('phone_num_1', models.CharField(max_length=250)),
                ('phone_num_2', models.CharField(max_length=250)),
                ('email_id_1', models.CharField(max_length=250)),
                ('email_id_2', models.CharField(max_length=250)),
                ('destination', models.CharField(max_length=250)),
                ('hotel', models.CharField(max_length=250)),
                ('room', models.CharField(max_length=250)),
                ('check_in', models.CharField(max_length=250)),
                ('check_out', models.CharField(max_length=250)),
                ('tours', models.TextField(max_length=250)),
                ('transfers', models.TextField(max_length=250)),
                ('inclusions', models.TextField(max_length=250)),
                ('price_quoted_in_foreign_currency', models.CharField(max_length=250)),
                ('foreign_currency', models.CharField(max_length=250)),
                ('price_quoted_in_inr', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
