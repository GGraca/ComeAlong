from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^$', ProjectsIndex.as_view()),
    url(r'^new/$', CreateProjectView.as_view()),
    url(r'^(?P<id>\d+)/$', ProjectPageView.as_view()),
    url(r'^(?P<id>\d+)/edit/$', UpdateProjectView.as_view()),
    url(r'^(?P<id>\d+)/recruit/$', recruit),
    url(r'^(?P<id>\d+)/follow/$', follow),
    url(r'^(?P<id>\d+)/unfollow/$', unfollow),
    url(r'^(?P<id>\d+)/apply/$', apply),
    url(r'^(?P<id>\d+)/delete/$', delete_project),
    url(r'^(?P<id>\d+)/applications', applications),
    url(r'^(?P<id>\d+)/(?P<app_id>\d+)/$', application),
)
