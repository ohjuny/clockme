# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-13 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='default_name', max_length=50),
        ),
    ]
