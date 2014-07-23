# ****** Sharing URLS.py ***********

from django.conf.urls import patterns, url
from sharing import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^register/$', views.register, name='register'),
        url(r'^sign_in/$', views.sign_in, name='sign_in'),
        url(r'^add_item/$', views.add_item, name='add_item'),
        url(r'^sign_out/$', views.sign_out, name='sign_out'),

)