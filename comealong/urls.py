from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *
import notifications

from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', Index.as_view(), name='index'),
    url(r'^about/$', About.as_view(), name='about'),
    url(r'^features/$', Features.as_view(), name='features'),
    url(r'^users/', include("my_user.urls")),
    url(r'^projects/', include("project.urls")),

    url(r'^admin/', include(admin.site.urls)),

    url('', include('social.apps.django_app.urls', namespace='social')),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'index.html'}, name="login"),
    url(r'^login/$', login_view, name="login"),
    url(r'^register/$', register_view, name="register"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name':'index.html'}, name="logout"),

    url('^inbox/notifications/', include(notifications.urls)),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
