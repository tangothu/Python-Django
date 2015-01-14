# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InterviewService', '0009_auto_20141216_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='computer_skills',
            field=models.TextField(default=b'computer_skills', null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='education_requirement',
            field=models.TextField(default=b'education_requirement', null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_description',
            field=models.TextField(default=b'Job Description', null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='key_accountabilities',
            field=models.TextField(default=b'key_accountabilities', null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='other_requirement',
            field=models.TextField(default=b'other_requirement', null=True),
        ),
    ]
