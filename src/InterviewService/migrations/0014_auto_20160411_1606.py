# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewService', '0013_auto_20141222_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]