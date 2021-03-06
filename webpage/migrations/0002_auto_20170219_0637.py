# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-19 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instagramaccount',
            name='photo',
        ),
        migrations.AddField(
            model_name='instagramaccount',
            name='photo',
            field=models.ManyToManyField(null=True, to='webpage.Photo'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='comments',
            field=models.ManyToManyField(null=True, to='webpage.Comment'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='tag',
            field=models.ManyToManyField(null=True, to='webpage.Tags'),
        ),
    ]
