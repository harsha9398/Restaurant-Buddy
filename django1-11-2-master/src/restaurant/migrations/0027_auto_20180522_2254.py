# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-22 17:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0026_dish_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
    ]
