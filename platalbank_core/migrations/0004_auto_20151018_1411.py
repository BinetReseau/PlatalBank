# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('platalbank_core', '0003_auto_20151013_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 10, 18, 14, 11, 6, 911348, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 10, 18, 14, 11, 15, 102151, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
