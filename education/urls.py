__author__ = 'eli'

from django.conf.urls import patterns,  url

from education import views

urlpatterns = patterns('',
    url(r'university', views.university),

    url(r'polytechnic', views.polytechnic),

    url(r'high_school', views.high_school),

    url(r'vocational', views.vocational),
)
