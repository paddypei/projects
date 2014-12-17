# -*-coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import todo.views
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    url(r'^$', include('todo.urls')),
    url(r'^todos/', include('todo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^listdata/$', todo.views.listdata, name='listdata'),
    url(r'^book/$', include('books.urls')),
    #url(r'^__debug__/', include(debug_toolbar.urls)),
)
