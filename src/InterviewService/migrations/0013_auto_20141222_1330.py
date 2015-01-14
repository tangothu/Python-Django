# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewService', '0012_auto_20141222_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewer',
            name='email',
            field=models.EmailField(max_length=75),
        ),
    ]
