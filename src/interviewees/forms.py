from django import forms
from django.contrib.auth.models import User
from interviewees.models import Interviewee
from InterviewService.models import Interview, Job, Company, Interviewer, Question, Department, Category
from registration.forms import RegistrationForm
from django.forms.models import inlineformset_factory


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        exclude= ('email',)
        fields = ('username', 'password')
        username = forms.EmailField(max_length=64,help_text = "The person's email address.")
    def clean_email( self ):
        email= self.cleaned_data['username']
        return email
    
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title','level','category','company','department','key_accountabilities','education_requirement','computer_skills')
        #fields = ('company','department','category')
    """
    def __init__(self, *args, **kwargs):
        self._company = kwargs.pop('company', None)
        self._department = kwargs.pop('department',None)
        self._title = kwargs.pop('title',None)
        super(JobForm, self).__init__(*args, **kwargs)
    def save(self, commit=True):
        inst = super(JobForm, self).save(commit=False)
        inst.company = self._company
        inst.department = self._department
        inst.title = self._title
        if commit:
            inst.save()
            self.save_m2m()
        return inst
    """    
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name','country')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category','description')

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name','function')
                
class InterviewerForm(forms.ModelForm):
    class Meta:
        model = Interviewer
        fields = ('first_name','last_name','interviewer_title','email','contact_info','race','personality')
        
        
class IntervieweeForm(forms.ModelForm):
    class Meta:
        model = Interviewee
    
    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user', None)
        super(IntervieweeForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(IntervieweeForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst

class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ('type','round','date')

    def __init__(self, *args, **kwargs):
        self._job = kwargs.pop('job', None)
        self._interviewee = kwargs.pop('interviewee',None)
        self._interviewer = kwargs.pop('interviewer',None)
        super(InterviewForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(InterviewForm, self).save(commit=False)
        inst.job = self._job
        inst.interviewee = self._interviewee
        inst.interviewer = self._interviewer
        if commit:
            inst.save()
            self.save_m2m()
        return inst

QuestionFormSet = inlineformset_factory(Interview,Question,extra=1,max_num=1,can_delete=False)