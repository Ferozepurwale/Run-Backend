# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hacku', '0002_auto_20170325_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='runuser',
            name='random_array',
            field=models.CharField(default=django.utils.timezone.now, max_length=10000),
            preserve_default=False,
        ),
    ]