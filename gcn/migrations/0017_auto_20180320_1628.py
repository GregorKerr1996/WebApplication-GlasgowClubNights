# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 16:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gcn', '0016_auto_20180320_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nightform',
            name='club_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]