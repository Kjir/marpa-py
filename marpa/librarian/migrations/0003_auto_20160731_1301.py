# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0002_auto_20160731_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='patron',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarian.Patron'),
        ),
    ]