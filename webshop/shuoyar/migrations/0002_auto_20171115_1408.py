# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuoyar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auther',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='auther',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]