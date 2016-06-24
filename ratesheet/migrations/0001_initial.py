# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratesheet.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratesheet.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cost', models.CharField(max_length=250)),
                ('currency', models.CharField(max_length=250)),
                ('valid_from', models.DateField(blank=True, null=True)),
                ('valid_until', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratesheet.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=255)),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('duration', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='rate',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratesheet.Room'),
        ),
        migrations.AddField(
            model_name='rate',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratesheet.Supplier'),
        ),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratesheet.Region'),
        ),
    ]
