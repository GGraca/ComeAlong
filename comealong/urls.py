from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', views.index, name="index"),
    url(r'^users/', include("my_user.urls")),
    url(r'^projects/', include("project.urls")),

    url(r'^admin/', include(admin.site.urls)),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
