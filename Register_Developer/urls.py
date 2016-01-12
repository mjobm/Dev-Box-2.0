from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from Register_Developer import views

urlpatterns = [
    url(r'me/$', views.profile),
    url(r'edit/$', views.edit_profile),
    url(r'new/portfolio$', views.new_portfolio),
    url(r'create/$', views.create_profile),
    url(r'create/portfolio/$', views.create_portfolio),
]
# urlpatterns = patterns('',
#
#     (r'$',views.profile),
#     (r'edit/',views.edit_profile),
#
#     (r'new/portfolio$',views.new_portfolio),
#
#     (r'create/$',views.create_profile),
#     (r'create/portfolio/$',views.create_portfolio),
#
# ) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
