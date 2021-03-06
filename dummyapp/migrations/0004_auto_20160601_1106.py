# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 05:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dummyapp', '0003_auto_20160530_2027'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hotel',
            new_name='Accommodation',
        ),
        migrations.RemoveField(
            model_name='inclusionrate',
            name='inclusion',
        ),
        migrations.RemoveField(
            model_name='inclusionrate',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='pricesearch',
            name='rate_of_exhange',
        ),
        migrations.RemoveField(
            model_name='pricesearch',
            name='room',
        ),
        migrations.RemoveField(
            model_name='pricesearch',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='roomrate',
            name='room',
        ),
        migrations.RemoveField(
            model_name='roomrate',
            name='supplier',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='hotel',
            new_name='accommodation',
        ),
        migrations.RemoveField(
            model_name='package',
            name='query',
        ),
        migrations.RemoveField(
            model_name='package',
            name='room_rate',
        ),
        migrations.AddField(
            model_name='package',
            name='default_inclusion',
            field=models.ManyToManyField(blank=True, related_name='package_default_inclusion', to='dummyapp.Inclusion'),
        ),
        migrations.AddField(
            model_name='package',
            name='optional_inclusion',
            field=models.ManyToManyField(blank=True, related_name='package_optional_inclusion', to='dummyapp.Inclusion'),
        ),
        migrations.AddField(
            model_name='package',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dummyapp.Room'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_rate_hash',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='inclusion',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='package',
            name='budget_type',
            field=models.CharField(choices=[('ECO', 'ECO'), ('DELX', 'DELX'), ('LUX', 'LUX')], max_length=255),
        ),
        migrations.AlterField(
            model_name='package',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='InclusionRate',
        ),
        migrations.DeleteModel(
            name='PriceSearch',
        ),
        migrations.DeleteModel(
            name='RateOfExchange',
        ),
        migrations.DeleteModel(
            name='RoomRate',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]
