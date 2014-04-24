from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'home.views.homePage', name='index'),

    url(r'^finance/', include('finance.urls')),

    url(r'^food/', include('food.urls')),

    url(r'^education/', include('education.urls')),

    url(r'^health/', include('health.urls')),

    url(r'^tech/', include('tech.urls')),
)





