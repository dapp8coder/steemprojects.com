# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-14 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20170814_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='steem_account',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True, verbose_name='Steem account'),
        ),
    ]