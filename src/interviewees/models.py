from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User

class Interviewee(models.Model):
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return self.user.username