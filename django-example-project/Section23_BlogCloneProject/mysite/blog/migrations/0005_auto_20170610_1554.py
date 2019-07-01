# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-10 15:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170610_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 10, 15, 54, 30, 980709, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 10, 15, 54, 30, 979933, tzinfo=utc)),
        ),
    ]
