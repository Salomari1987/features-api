# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('target_date', models.DateField(blank=True)),
                ('ticket_url', models.URLField()),
                ('product_area', models.CharField(choices=[('P', 'Policies'), ('B', 'Billing'), ('C', 'Claims'), ('R', 'Reports')], max_length=2)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
