# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewService', '0003_auto_20141116_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='slug',
        ),
    ]
