# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-20 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20170418_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcategory',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
