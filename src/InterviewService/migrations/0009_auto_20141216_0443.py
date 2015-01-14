# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewService', '0008_auto_20141215_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_posting_url',
            field=models.URLField(null=True),
        ),
    ]
