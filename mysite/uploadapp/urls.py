from django.conf.urls import patterns, include, url
from mysite.uploadapp import views

urlpatterns = patterns('uploadapp.views',
    url(r'^$', views.UploadAlfabet.as_view(), name='uploadalfabet'),

)
