from django.conf.urls import patterns, include, url
from views import *

comments = patterns('',
    #url(r'^teste/$', teste),
    #url(r'^new/$', comment),
    #url(r'^(?P<comment_id>\d+)/edit/$', edit),
    #url(r'^(?P<comment_id>\d+)/delete/$', delete),
)

#Vacancies
vacancies = patterns('',
    url(r'^$', ProjectsIndex.as_view()),
    url(r'^new/$', CreateVacancyView.as_view()),
    #url(r'^(?P<vacancy_id>\d+)/edit/$', edit),
    #url(r'^(?P<vacancy_id>\d+)/delete/$', delete),
)

#Projects
urlpatterns = patterns('',
    url(r'^$', ProjectsIndex.as_view()),

    url(r'^new/$', CreateProjectView.as_view()),
    url(r'^(?P<id>\d+)/edit/$', UpdateProjectView.as_view()),
    url(r'^(?P<id>\d+)/delete/$', delete_project),

    url(r'^(?P<id>\d+)/$', ProjectPageView.as_view()),

    url(r'^(?P<id>\d+)/follow/$', follow),
    url(r'^(?P<id>\d+)/unfollow/$', unfollow),

    url(r'^(?P<id>\d+)/vacancies/', include(vacancies)),
    #url(r'^(?P<id>\d+)/recruit/$', recruit),

    url(r'^(?P<id>\d+)/apply/$', apply),
    url(r'^(?P<id>\d+)/applications', applications),
    url(r'^(?P<id>\d+)/(?P<app_id>\d+)/$', application),
    url(r'^(?P<project_id>\d+)/topics/', include("topic.urls")),
)
