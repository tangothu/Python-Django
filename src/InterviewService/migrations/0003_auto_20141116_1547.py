# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewService', '0002_auto_20141114_0307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interviewer',
            old_name='title',
            new_name='interviewer_title',
        ),
    ]
