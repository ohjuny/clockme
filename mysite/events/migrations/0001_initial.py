# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-13 22:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='FreeTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='free_times',
            field=models.ManyToManyField(to='events.FreeTime'),
        ),
        migrations.AddField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]