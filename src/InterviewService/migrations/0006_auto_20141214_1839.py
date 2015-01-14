# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewService', '0005_auto_20141214_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='shortname',
            field=models.CharField(default=b'Short Name', max_length=256, null=True),
        ),
    ]
