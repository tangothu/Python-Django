from django.contrib import admin

# Register your models here.
from .models import Interviewee

class IntervieweeAdmin(admin.ModelAdmin):
    class Meta:
        model = Interviewee
        
admin.site.register(Interviewee,IntervieweeAdmin)