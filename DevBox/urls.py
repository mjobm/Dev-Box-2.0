"""DevBox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import Register_Developer
from . import views
admin.autodiscover()

urlpatterns = patterns('',

    (r'^$',views.home_page),
    (r'^start/$',views.get_started),
    ('', include('social.apps.django_app.urls', namespace='social')),
    (r'^dev/',include('DevBoxLogin.urls')),
    (r'^dev/profile/', include('Register_Developer.urls')),
    (r'^emp/', include('Register_Employer.urls')),
    (r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
