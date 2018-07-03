from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^viewall/$', views.viewAll, name='view all'),
    url(r'^viewall/([\s\w]+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create, name='create')
]
