# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('pages', models.IntegerField()),
                ('published_on', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('published_on', 'title'),
            },
        ),
    ]
