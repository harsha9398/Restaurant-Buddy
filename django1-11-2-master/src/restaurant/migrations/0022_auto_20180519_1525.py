# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-19 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0021_restaurantlocation_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Mandatory', max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('Veg', 'Veg'), ('Non-veg', 'Non-veg')], max_length=7)),
            ],
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(choices=[('Veg', 'Veg'), ('Non-veg', 'Non-veg')], max_length=7),
        ),
    ]
