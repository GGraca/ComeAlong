from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^(?P<username>\w+)/$', views.page),
    url(r'^(?P<username>\w+)/edit/$', views.edit),
)
