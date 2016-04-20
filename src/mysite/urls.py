from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView
from interviewees import views

class MyRegistrationView(RegistrationView):
    def get_success_url(selfself,request, user):
        return '/'

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
    #url(r'^about-us/$', 'signups.views.aboutus', name='aboutus'),
    #url(r'^interview_submit/$', 'interviewees.views.interview_submit', name='interview_submit'),
    url(r'^restricted/$', 'interviewees.views.restricted', name='restricted'),
    (r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    
    url(r'^interview_list/$', views.interview_list, name='interview_list'),
    url(r'^interview_list/new$', views.interview_create, name='interview_new'),
    url(r'^interview_list/edit/(?P<pk>\d+)$', views.interview_update, name='interview_edit'),
    url(r'^interview_list/delete/(?P<pk>\d+)$', views.interview_delete, name='interview_delete'),
    
    url(r'^search_interviews/$', views.search_interviews, name='search_interviews'),
    
    url(r'^company_new/new$', views.company_create, name='company_new'),
    url(r'^department_new/new$', views.department_create, name='department_new'),
    url(r'^category_new/new$', views.category_create, name='category_new'),
    
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
