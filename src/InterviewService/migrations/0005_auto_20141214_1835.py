# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewService', '0004_remove_job_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='shortname',
            field=models.CharField(default=b'Short Name', max_length=256, unique=True, null=True),
        ),
    ]
