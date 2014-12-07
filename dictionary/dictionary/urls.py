from django.conf.urls import patterns, include, url
from dict import views
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

# if settings.DEBUG:
#     urlpatterns = patterns('',
#     url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#     url(r'', include('django.contrib.staticfiles.urls')),
# ) + urlpatterns

urlpatterns = i18n_patterns('',
    url(r'^upload/?', include('uploadapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)