from django.conf.urls import patterns,  url

from django.contrib import admin

from finance import views

admin.autodiscover()

urlpatterns = patterns('',

    url(r'banks', views.banks),

#    url(r'^banks', BankListView.as_view()),

#    url(r'$', views.index),

#    url(r'/micro_finance', views.micro_finance),

#    url(r'/savings_n_loans', views.savings_n_loans),
)
