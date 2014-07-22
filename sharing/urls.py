# ****** Sharing URLS.py ***********

from django.conf.urls import patterns, url
from sharing import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^register/$', views.register, name='register'),
        url(r'^add_item/$', views.add_item, name='add_item'),
)

