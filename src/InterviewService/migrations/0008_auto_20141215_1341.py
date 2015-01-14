# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewService', '0007_auto_20141215_0343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='years_experience_required',
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(default=b'Department Name', unique=True, max_length=512),
        ),
    ]
