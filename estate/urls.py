from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'estate.views.home', name='home'),
]