from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^$', UsersIndex.as_view()),
    url(r'^(?P<username>\w+)/$', UserPageView.as_view()),
    url(r'^(?P<username>\w+)/edit/$', UserUpdateView.as_view()),
)
