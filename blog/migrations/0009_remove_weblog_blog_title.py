# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-15 13:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_weblog_blog_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weblog',
            name='blog_title',
        ),
    ]
