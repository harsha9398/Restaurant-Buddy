# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-19 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0022_auto_20180519_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
