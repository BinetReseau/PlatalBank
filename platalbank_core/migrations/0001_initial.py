# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('balance', models.DecimalField(max_digits=20, decimal_places=2)),
                ('description', models.CharField(max_length=1024)),
                ('short_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=1024)),
                ('through_khube', models.BooleanField()),
                ('writable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('state', models.CharField(choices=[('P', 'PENDING'), ('A', 'AUTHORIZED'), ('R', 'REJECTED'), ('X', 'ABORTED'), ('C', 'COMPLETED')], max_length=1, default='P')),
                ('amount', models.DecimalField(max_digits=20, decimal_places=2)),
                ('label', models.CharField(max_length=1024)),
                ('credited_account', models.ForeignKey(related_name='in_transactions', to='platalbank_core.Account')),
                ('debited_account', models.ForeignKey(related_name='out_transactions', to='platalbank_core.Account')),
                ('event', models.ForeignKey(to='platalbank_core.Event')),
            ],
        ),
    ]
