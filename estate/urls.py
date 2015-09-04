from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'estate.views.home', name='home'),
    url(r'^about/$', 'estate.views.about', name='about'),
]