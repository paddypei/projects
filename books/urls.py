from django.contrib import admin
from django.conf.urls import patterns, url
from books import views
urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^list_book/$', views.list_book, name='list_book'),
)
