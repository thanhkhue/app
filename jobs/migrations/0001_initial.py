# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=30)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=10)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10)),
                ('image', models.ImageField(upload_to='static/jobs/image')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=100)),
                ('activate', models.BooleanField(default=False)),
            ],
        ),
    ]
