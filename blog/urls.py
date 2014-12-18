# -*-coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    #url(r'^$', include('todo.urls')),
    url(r'^todos/', include('todo.urls')),
    #此处不能以$结尾
    url(r'^book/', include('books.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^grappelli/',include('grappelli.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^__debug__/', include(debug_toolbar.urls)),
)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),

    )
