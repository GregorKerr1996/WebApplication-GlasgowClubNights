# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcn', '0021_userreviewform_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreviewform',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
