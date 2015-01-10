from django.conf.urls import patterns, include, url
from views import *

#Comments
comments = patterns('',
    #url(r'^teste/$', teste),
    #url(r'^new/$', comment),
    #url(r'^(?P<comment_id>\d+)/edit/$', edit),
    #url(r'^(?P<comment_id>\d+)/delete/$', delete),
)

#Topics
urlpatterns = patterns('',
    #url(r'^(?P<app_id>\d+)/$', TopicPageView.as_view()),
    #url(r'^new/$', new,
    #url(r'^(?P<topic_id>\d+)/edit/$', edit,
    #url(r'^(?P<topic_id>\d+)/delete/$', delete,
    url(r'^(?P<topic_id>\d+)/comments/', include(comments)),
)
