# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 10:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Testtable',
            new_name='Table',
        ),
        migrations.AlterModelTable(
            name='table',
            table=None,
        ),
    ]