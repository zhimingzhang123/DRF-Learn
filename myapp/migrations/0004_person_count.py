# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-18 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20181116_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
