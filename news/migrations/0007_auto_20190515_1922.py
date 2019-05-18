# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-15 16:22
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20190515_1635'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Editor',
        ),
        migrations.AlterField(
            model_name='article',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
    ]
