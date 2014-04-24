__author__ = 'eli'

from django.conf.urls import patterns,  url

from tech import views

urlpatterns = patterns('',
    url(r'telcos', views.telcos),

    url(r'content_providers', views.content_providers),

)



