# *******Share_Stuff Project urls.py********

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'share_stuff.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sharing/', include('sharing.urls')),
)

    # url(r'^rango/', include('rango.urls')), # ADD THIS NEW TUPLE!

