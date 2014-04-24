__author__ = 'eli'

from django.conf.urls import patterns,  url

from health import views

urlpatterns = patterns('',
    url(r'traditional', views.traditional),

    url(r'pharmacy', views.pharmacy),

    url(r'chemist', views.chemist),

    url(r'hospital', views.hospital),
)



