from django.conf.urls import patterns, include, url
from django.contrib import admin
from dict import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dict.views.home', name='home'),
    url(r'^upload/?', include('uploadapp.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
