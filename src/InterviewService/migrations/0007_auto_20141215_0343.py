# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewService', '0006_auto_20141214_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='company',
            field=models.ForeignKey(to='InterviewService.Company', null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='manager',
            field=models.ForeignKey(to='InterviewService.Interviewer', null=True),
        ),
    ]
