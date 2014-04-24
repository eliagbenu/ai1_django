__author__ = 'eli'

from django.conf.urls import patterns,  url

from django.contrib import admin

from food import views

admin.autodiscover()

urlpatterns = patterns('',

    url(r'restaurant', views.restaurant),

)

