# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-27 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('v_rate', '0005_auto_20201027_1305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AddField(
            model_name='project',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]