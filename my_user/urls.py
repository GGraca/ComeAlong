from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^all/$', views.all),
    url(r'^(?P<username>\w+)/$', views.user),
)
