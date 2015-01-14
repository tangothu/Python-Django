# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewService', '0011_auto_20141222_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_description',
            field=models.TextField(default=b'Job Description', null=True),
        ),
    ]
