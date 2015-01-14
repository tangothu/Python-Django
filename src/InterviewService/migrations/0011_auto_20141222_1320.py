# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewService', '0010_auto_20141222_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewer',
            name='email',
            field=models.EmailField(default=b'example@company.com', max_length=75),
        ),
        migrations.AlterField(
            model_name='job',
            name='computer_skills',
            field=models.TextField(default=b'computer_skills'),
        ),
        migrations.AlterField(
            model_name='job',
            name='education_requirement',
            field=models.TextField(default=b'education_requirement'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_description',
            field=models.TextField(default=b'Job Description'),
        ),
        migrations.AlterField(
            model_name='job',
            name='key_accountabilities',
            field=models.TextField(default=b'key_accountabilities'),
        ),
        migrations.AlterField(
            model_name='job',
            name='other_requirement',
            field=models.TextField(default=b'other_requirement'),
        ),
    ]
