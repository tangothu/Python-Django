from django.contrib import admin

# Register your models here.

from InterviewService.models import Industry, Company, Interviewer
from InterviewService.models import Department, Job, Interview, Question, Category
from interviewees.models import Interviewee

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0

class InterviewAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Job', {'fields': ['job']}),
        ('Type', {'fields': ['type']}),
        ('Round', {'fields': ['round']}),
        ('Interviewer', {'fields': ['interviewer']}),
        ('Date information', {'fields': ['date'], 'classes': ['collapse']}),
        ('Interviewee', {'fields': ['interviewee']}),
    ]
    inlines = [QuestionInline]

admin.site.register(Industry)
admin.site.register(Company)
admin.site.register(Interviewer)
admin.site.register(Category)
admin.site.register(Department)
admin.site.register(Job)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(Question)