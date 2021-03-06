# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 14:02
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
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dummyapp.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dummyapp.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='Inclusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dummyapp.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='InclusionRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('cost', models.CharField(max_length=250)),
                ('currency', models.CharField(max_length=250)),
                ('valid_from', models.DateField(blank=True, null=True)),
                ('valid_until', models.DateField(blank=True, null=True)),
                ('inclusion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dummyapp.Inclusion')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('duration', models.IntegerField()),
                ('budget_type', models.CharField(max_length=250)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dummyapp.Destination')),
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
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dummyapp.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='RoomRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('meal_plan', models.CharField(max_length=250)),
                ('inclusion', models.TextField(blank=True, max_length=250)),
                ('cost', models.CharField(max_length=250)),
                ('currency', models.CharField(max_length=250)),
                ('valid_from', models.DateField(blank=True, null=True)),
                ('valid_until', models.DateField(blank=True, null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dummyapp.Room')),
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
            model_name='roomrate',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dummyapp.Supplier'),
        ),
        migrations.AddField(
            model_name='package',
            name='query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dummyapp.Search'),
        ),
        migrations.AddField(
            model_name='inclusionrate',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dummyapp.Supplier'),
        ),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dummyapp.Region'),
        ),
    ]
