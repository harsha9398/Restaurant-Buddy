# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-16 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_restaurantlocation_year_in_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.CharField(max_length=4)),
            ],
        ),
    ]
