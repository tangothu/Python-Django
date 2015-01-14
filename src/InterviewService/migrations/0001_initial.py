# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('interviewees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(unique=True, max_length=256)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Company Name', unique=True, max_length=512)),
                ('shortname', models.CharField(default=b'Short Name', unique=True, max_length=256)),
                ('country', models.CharField(default=b'Canada', max_length=256)),
                ('description', models.TextField(default=b'Description')),
                ('views', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Department Name', max_length=512)),
                ('shortname', models.CharField(default=b'Dept Short Name', max_length=256)),
                ('function', models.TextField(default=b'team_function')),
                ('company', models.ForeignKey(to='InterviewService.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('industry', models.CharField(unique=True, max_length=256)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'InPerson', max_length=128, choices=[(b'Phone', b'Phone'), (b'Online', b'Online'), (b'InPerson', b'InPerson')])),
                ('round', models.IntegerField(default=1)),
                ('date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('interviewee', models.ForeignKey(to='interviewees.Interviewee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Interviewer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'First Name', max_length=128)),
                ('last_name', models.CharField(default=b'Last Name', max_length=128)),
                ('title', models.CharField(default=b'Manager', max_length=128, choices=[(b'Analyst', b'Analyst'), (b'Developer', b'Developer'), (b'Associate', b'Associate'), (b'Manager', b'Manager'), (b'Senior Manager', b'Senior Manager'), (b'AVP', b'AVP'), (b'VP', b'VP'), (b'SVP', b'SVP'), (b'EVP', b'EVP'), (b'Director', b'Director'), (b'Managing Director', b'Managing Director'), (b'Executive', b'Executive')])),
                ('email', models.EmailField(max_length=75)),
                ('contact_info', models.CharField(default=b'Contact info', max_length=256)),
                ('race', models.CharField(default=b'Race', max_length=128)),
                ('personality', models.CharField(default=b'personality', max_length=512)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Job Title', max_length=128)),
                ('level', models.CharField(default=b'Entry', max_length=128, choices=[(b'Senior', b'Senior'), (b'Junior', b'Junior'), (b'Entry', b'Entry'), (b'People Manager', b'People Manager')])),
                ('key_accountabilities', models.TextField(default=b'key_accountabilities')),
                ('education_requirement', models.TextField(default=b'education_requirement')),
                ('other_requirement', models.TextField(default=b'other_requirement')),
                ('computer_skills', models.TextField(default=b'computer_skills')),
                ('years_experience_required', models.IntegerField(default=1)),
                ('job_posting_url', models.URLField()),
                ('job_description', models.TextField(default=b'Job Description')),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(to='InterviewService.Category')),
                ('company', models.ForeignKey(to='InterviewService.Company', null=True)),
                ('department', models.ForeignKey(to='InterviewService.Department', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Brief Description of the Question', max_length=256)),
                ('question', models.TextField(default=b'Question Detail Here')),
                ('type', models.CharField(default=b'Written', max_length=128)),
                ('answer', models.TextField(default=b'Question Detail Here')),
                ('interview', models.ForeignKey(to='InterviewService.Interview')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='interview',
            name='interviewer',
            field=models.ForeignKey(to='InterviewService.Interviewer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='interview',
            name='job',
            field=models.ForeignKey(to='InterviewService.Job'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='department',
            name='manager',
            field=models.ForeignKey(to='InterviewService.Interviewer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='department',
            name='parent_department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='InterviewService.Department', null=True),
            preserve_default=True,
        ),
    ]
