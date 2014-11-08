from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^new/$', views.new),
    url(r'^(?P<id>\d+)/$', views.page),
    url(r'^(?P<id>\d+)/apply/$', views.new_application),
    url(r'^(?P<id>\d+)/(?P<app_id>\d+)$', views.application),
)
