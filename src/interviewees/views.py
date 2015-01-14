from interviewees.forms import UserForm, InterviewForm, IntervieweeForm, InterviewerForm, JobForm, CompanyForm, DepartmentForm, CategoryForm, QuestionFormSet
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from InterviewService.models import Job, Interview, Interviewer, Company, Department, Category
from django.contrib.auth.models import User
from interviewees.models import Interviewee
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, RequestContext, redirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse_lazy
import pdb

@login_required
def interview_list(request, template_name='InterviewService/interview_list.html'):
    interviewee = Interviewee.objects.get_or_create(user=request.user)[0]
    interviews = Interview.objects.filter(interviewee=interviewee)
    
    if request.user.username=='admin':
        interviews = Interview.objects.all()
    
    data = {}
    data['object_list'] = interviews
    return render(request, template_name, data)

@login_required
def search_interviews(request, template_name='InterviewService/interview_list.html'):
    if request.GET:
        search_term = request.GET['term']
        interviewee = Interviewee.objects.get_or_create(user=request.user)[0]
        
        if request.user.username!='admin':
            job_results = Interview.objects.filter(job__title__contains=search_term).filter(interviewee=interviewee)
            interviewee_results = Interview.objects.filter(interviewee__user__username__contains=search_term).filter(interviewee=interviewee)
        
        else:
            job_results = Interview.objects.filter(job__title__contains=search_term)
            interviewee_results = Interview.objects.filter(interviewee__user__username__contains=search_term)

        results = job_results | interviewee_results
        data = {}
        data['object_list'] = results
        return render(request, template_name, data)

@login_required
def interview_create(request, template_name='InterviewService/interview_form.html'):
    company = None
    department = None
    category = None
    
    if request.method == 'POST':
        if 'company' in request.session:
            company = request.session['company']
        if 'department' in request.session:
            department = request.session['department']
        if 'category' in request.session:
            category = request.session['category']
        
        if company != None or department != None or category != None:
            #data={'company':company,'department':department,'title':'Job Title'}
            job_form = JobForm(request.POST or None,initial={'company': company, 'department': department, 'category': category, })
            #job_form = JobForm(request.POST or None,data)
        else:
            job_form = JobForm(data=request.POST)

        
        interview_form = InterviewForm(request.POST)
        interviewer_form = InterviewerForm(request.POST)
        question_form = QuestionFormSet(request.POST)
        
        
        if interview_form.is_valid() and job_form.is_valid() and interviewer_form.is_valid() and question_form.is_valid(): 
            job = job_form.save(commit=False)
            job.title = request.POST['title']
            job.company = Company.objects.get(id=request.POST['company'])
            job.department = Department.objects.get(id=request.POST['department'])
            job.category = Category.objects.get(id=request.POST['category'])

            job.level = request.POST['level']
            job.key_accountabilities = request.POST['key_accountabilities']
            job.education_requirement = request.POST['education_requirement']
            job.computer_skills = request.POST['computer_skills']
            job.save()
            
            interviewee = Interviewee.objects.get_or_create(user=request.user)[0]
            interviewee.save()
            
            interviewer = interviewer_form.save(commit=False)
            interviewer.save()
            
            interview_form = InterviewForm(data=request.POST,job=job,interviewee=interviewee,interviewer=interviewer)
            
            interview = interview_form.save(commit=False)
            interview.save()
            
            question_form = QuestionFormSet(data=request.POST, instance=interview)
            question_form.save()
            
            return redirect(interview_list)
        
        else:
            print job_form.errors
            print interview_form.errors
            print interviewer_form.errors
            print question_form.errors
            

    else:
        
        if 'company' in request.session:
            company = request.session['company']
        if 'department' in request.session:
            department = request.session['department']
        if 'category' in request.session:
            category = request.session['category']
        
        if company != None or department != None or category != None:
            #data={'company':company,'department':department,'title':'Job Title'}
            job_form = JobForm(request.POST or None,initial={'company': company, 'department': department, 'category': category, })
            #job_form = JobForm(request.POST or None,data)
        else:
            job_form = JobForm(request.POST)
        
        interview_form = InterviewForm()
        interviewer_form = InterviewerForm()
        question_form = QuestionFormSet()
        
    return render(request, template_name, {
                'interview_form':interview_form,
                'interviewer_form':interviewer_form,
                'job_form':job_form,
                'question_form':question_form,
                })

@login_required
def interview_update(request, pk, template_name='InterviewService/interview_form.html'):
    
    company = None
    department = None
    category = None

    interview = get_object_or_404(Interview, pk=pk)
    job = get_object_or_404(Job, pk=interview.job.pk)
    interviewer = get_object_or_404(Interviewer, pk=interview.interviewer.pk)
    
    interview_form = InterviewForm(request.POST or None, instance=interview)
    job_form = JobForm(request.POST or None, instance=job)
    interviewer_form = InterviewerForm(request.POST or None, instance=interviewer)
    interviewee_form = IntervieweeForm(data=request.POST,user=request.user)
    question_form = QuestionFormSet(request.POST,instance=interview)

    if request.method == 'POST':
        
        if interview_form.is_valid() and job_form.is_valid() and interviewer_form.is_valid():# and question_form.is_valid():
            
            job = job_form.save(commit=False)
            job.title = request.POST['title']
            job.company = Company.objects.get(id=request.POST['company'])
            job.department = Department.objects.get(id=request.POST['department'])
            job.category = Category.objects.get(id=request.POST['category'])

            job.level = request.POST['level']
            job.key_accountabilities = request.POST['key_accountabilities']
            job.education_requirement = request.POST['education_requirement']
            job.computer_skills = request.POST['computer_skills']
            job.save()
    
            interviewee = Interviewee.objects.get_or_create(user=request.user)[0]
        
            interviewer = interviewer_form.save(commit=False)
            interviewer.save()
            
            interview_form = InterviewForm(data=request.POST,job=job,interviewee=interviewee,interviewer=interviewer)
            interview = interview_form.save(commit=False)
            interview.pk=pk
            interview.save()
        
            if question_form.is_valid():
               question_form.save()
        
            return redirect(interview_list)
        else:
            print job_form.errors
            print interview_form.errors
            print interviewer_form.errors
            print question_form.errors
    else:
        interview_form = InterviewForm(request.POST or None, instance=interview)
        job_form = JobForm(request.POST or None, instance=job)
        interviewer_form = InterviewerForm(request.POST or None, instance=interviewer)
        interviewee_form = IntervieweeForm(data=request.POST,user=request.user)
        question_form = QuestionFormSet(instance=interview)

    return render(request, template_name, {
                'interview_form':interview_form,
                'interviewer_form':interviewer_form,
                'job_form':job_form,
                'question_form':question_form,
                })

@login_required
def interview_delete(request, pk, template_name='InterviewService/interview_confirm_delete.html'):
    interview = get_object_or_404(Interview, pk=pk)
    if request.method=='POST':
        interview.delete()
        return redirect('interview_list')
    return render(request, template_name, {'object':interview})

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def company_create(request, template_name='InterviewService/object_form.html'):    
    interview_template='InterviewService/interview_form.html'
    if request.method == 'POST':
        object_form = CompanyForm(data=request.POST)
        if object_form.is_valid() :
            company = object_form.save(commit=False)
            company.save()
            request.session['company'] = company
            return redirect(interview_create)
    else:
        object_form = CompanyForm()
    object_meta = object_form.Meta.model.__name__
    return render(request, template_name, {
                'object_form':object_form,
                'object_meta':object_meta,
                })

@login_required
def department_create(request, template_name='InterviewService/object_form.html'):    
    if request.method == 'POST':
        object_form = DepartmentForm(data=request.POST)
        if object_form.is_valid() :
            department = object_form.save(commit=False)
            department.save()
            request.session['department'] = department
            return redirect(interview_create)
    else:
        object_form = DepartmentForm()
    object_meta = object_form.Meta.model.__name__
    return render(request, template_name, {
                'object_form':object_form,
                'object_meta':object_meta,
                })

@login_required
def category_create(request, template_name='InterviewService/object_form.html'):    
    if request.method == 'POST':
        object_form = CategoryForm(data=request.POST)
        if object_form.is_valid() :
            category = object_form.save(commit=False)
            category.save()
            request.session['category'] = category
            return redirect(interview_create)
    else:
        object_form = CategoryForm()
    object_meta = object_form.Meta.model.__name__
    return render(request, template_name, {
                'object_form':object_form,
                'object_meta':object_meta,
                })

"""
@login_required
def interview_submit(request):
    filled = False
    job_form = None
    interviewee_form = None
    interview_form = None
    interviewer_form = None
    
    #JobInlineFormSet = inlineformset_factory(Job, Interview, form=InterviewForm, extra=1)
    #jobInlineFormSet = JobInlineFormSet(request.POST)
    
    #IntervieweeInlineFormSet = inlineformset_factory(Interviewee, Interview, form=InterviewForm, extra=1)
    #intervieweeInlineFormSet = IntervieweeInlineFormSet(request.POST)
    
    if request.method == 'POST':
        
        job_form = JobForm(data=request.POST)
        interviewee_form = IntervieweeForm(data=request.POST,user=request.user)
        interview_form = InterviewForm(data=request.POST)
        interviewer_form = InterviewerForm(data=request.POST)

        #if job_form.is_valid() and interviewee_form.is_valid() and interview_form.is_valid():
        if job_form.is_valid() and interview_form.is_valid():
            
            job = job_form.save()
            job.save()
            
            #interviewee = interviewee_form.save()
            interviewee = Interviewee.objects.get_or_create(user=request.user)[0]
            interviewee.save()
            
            interviewer = interviewer_form.save(commit=False)
            interviewer.save()
            
            interview_form = InterviewForm(data=request.POST,job=job,interviewee=interviewee,interviewer=interviewer)
            
            interview = interview_form.save(commit=False)
            interview.job = job
            interview.interviewee = interviewee
            interview.save()

            #jobInlineFormSet = JobInlineFormSet(request.POST, instance=job)
            #intervieweeInlineFormSet =IntervieweeInlineFormSet(request.POST, instance=interviewee)
            
            #if jobInlineFormSet.is_valid() and intervieweeInlineFormSet.is_valid():
                
                #jobInlineFormSet.save()
                #intervieweeInlineFormSet.save()
            filled = True
            return render(request,
                    'interview_submit.html',
                    {'filled': filled,
                    'job_form': job_form,
                    #'interviewee_form': interviewee_form,
                    'interview_form': interview_form,
                    'interviewer_form': interviewer_form
                    })
            #else:
                #print jobInlineFormSet.errors
                #print intervieweeInlineFormSet.errors
        else:
            print job_form.errors
            #print interviewee_form.errors
            print interview_form.errors
            print interviewer_form.errors
    else:
        job_form = JobForm()
        #interviewee_form = IntervieweeForm()
        interview_form = InterviewForm()
        interviewer_form = InterviewerForm()
        #jobInlineFormSet = JobInlineFormSet()
        #intervieweeInlineFormSet = IntervieweeInlineFormSet()

    # Render the template depending on the context.
    return render(request,
            'interview_submit.html',
            {'filled': filled,
            'job_form': job_form,
            #'interviewee_form': interviewee_form,
            'interview_form': interview_form,
            'interviewer_form': interviewer_form
            })
"""