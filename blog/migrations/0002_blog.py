# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_id', models.IntegerField()),
                ('blog_num', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]