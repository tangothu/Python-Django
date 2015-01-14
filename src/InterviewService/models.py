from django.db import models
from datetime import datetime
from interviewees.models import Interviewee
from django.template.defaultfilters import slugify

# from .forms import StringListField

# Create your models here.

class Category(models.Model):
    category	= models.CharField(max_length=256, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.category

class Industry(models.Model):
    industry    = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.industry

class Company(models.Model):
    
    name        = models.CharField(max_length=512, default='Company Name', unique=True)
    shortname   = models.CharField(max_length=256, default='Short Name', null=True)
    #industry    = models.ForeignKey(Industry, null=True)
    country     = models.CharField(max_length=256, default='Canada')
    description = models.TextField(default='Description')
    views       = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Interviewer(models.Model):

    COMPANY_TITLE = (
        ('Analyst', 'Analyst'),
        ('Developer', 'Developer'),
        ('Associate', 'Associate'),
        ('Manager', 'Manager'),
        ('Senior Manager', 'Senior Manager'),
        ('AVP', 'AVP'),
        ('VP', 'VP'),
        ('SVP', 'SVP'),
        ('EVP', 'EVP'),
        ('Director', 'Director'),
        ('Managing Director', 'Managing Director'),
	('Executive','Executive'),
    )
    
    first_name   = models.CharField(max_length=128, default='First Name')
    last_name    = models.CharField(max_length=128, default='Last Name')  
    interviewer_title        = models.CharField(max_length=128, choices=COMPANY_TITLE, default='Manager')
    email        = models.EmailField()
    contact_info = models.CharField(max_length=256, default='Contact info')
    race         = models.CharField(max_length=128, default='Race')
    personality  = models.CharField(max_length=512, default='personality')
    
    def __str__(self):
        return u"%s %s" % (self.first_name, self.last_name)
	

    
        
class Department(models.Model):
    company             = models.ForeignKey(Company, null=True)
    name                = models.CharField(max_length=512, default='Department Name', unique=True)
    shortname           = models.CharField(max_length=256, default='Dept Short Name')
    function            = models.TextField(default='team_function')
    manager             = models.ForeignKey(Interviewer, null=True)
    parent_department   = models.ForeignKey("Department", blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
    
class Job(models.Model):
    
    JOB_LEVEL = (
        ('Senior', 'Senior'),
        ('Junior', 'Junior'),
        ('Entry', 'Entry'),
	('People Manager', 'People Manager'),
    )
        
    title                       = models.CharField(max_length=128, default='Job Title')
    level                       = models.CharField(max_length=128, choices=JOB_LEVEL, default='Entry')    
    category                    = models.ForeignKey(Category, null=True)
    company                     = models.ForeignKey(Company, null=True)
    department                  = models.ForeignKey(Department, null=True)
    key_accountabilities        = models.TextField(default='key_accountabilities')
    education_requirement       = models.TextField(default='education_requirement')
    other_requirement           = models.TextField(default='other_requirement')
    computer_skills             = models.TextField(default='computer_skills')
    
    #years_experience_required   = models.IntegerField(default=1)
    
    job_posting_url             = models.URLField(null=True)
    job_description             = models.TextField(default='Job Description', null=True)
    
    class Meta:
        verbose_name_plural = 'jobs'
    
    def __str__(self):
        return self.title
    

class Interview(models.Model):

    INTERVIEW_TYPE = (
        ('Phone', 'Phone'),
        ('Online', 'Online'),
        ('InPerson', 'InPerson'),
    )
    
    job         = models.ForeignKey(Job)   
    type        = models.CharField(max_length=128, choices=INTERVIEW_TYPE, default='InPerson')
    round       = models.IntegerField(default=1)
    date 	= models.DateTimeField(default=datetime.now, blank=True)
    interviewer = models.ForeignKey(Interviewer)
    #question	= models.ForeignKey(Question)
    #question = fields.EmbeddedModelField('Question')
    interviewee = models.ForeignKey(Interviewee)
    
    def __str__(self):
        return self.job.title+','+self.interviewee.user.username
    
    def __unicode__(self):
        return self.job.title

class Question(models.Model):
        
        name        = models.CharField(max_length=256, default='Brief Description of the Question')
        question    = models.TextField(default='Question Detail Here') 
        type        = models.CharField(max_length=128, default='Written')
        answer      = models.TextField(default='Question Detail Here')
        interview   = models.ForeignKey(Interview)
	
        def __str__(self):
            return self.name

