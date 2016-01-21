from django.conf.urls import include, url

from django.contrib import admin
from Register_Employer import views

admin.autodiscover()
urlpatterns = [
    url(r'accounts/', include('allauth.urls')),
    url(r'auth/', include('registration.backends.default.urls')),
    url(r'home/$', views.emp_home),
    url(r'create/$', views.register_employer),
    url(r'job/$', views.show_job_form),
    url(r'job/post/$', views.post_job),
]
