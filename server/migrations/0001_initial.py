# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(default='No description provided.')),
                ('provider', models.CharField(max_length=255)),
            ],
        ),
    ]
