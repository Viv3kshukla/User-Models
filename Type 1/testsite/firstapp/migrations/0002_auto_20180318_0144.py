# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-17 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='extra_info',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('driver', 'driver'), ('official', 'official'), ('person', 'person')], default='driver', max_length=20),
        ),
    ]
