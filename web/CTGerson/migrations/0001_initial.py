# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-05 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=8)),
                ('linenumber', models.CharField(max_length=5)),
                ('company', models.CharField(max_length=100)),
            ],
        ),
    ]
