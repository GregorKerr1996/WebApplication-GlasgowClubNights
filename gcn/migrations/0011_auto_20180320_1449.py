# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gcn', '0010_auto_20180320_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='night',
            name='club_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gcn.Club'),
        ),
    ]