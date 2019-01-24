#dojo/urls.py
from django.conf.urls import url
from django.urls import path, re_path

from dojo import views

urlpatterns = [
    re_path(r'^sum/(?P<x>\d+)/$', views.mysum),
    re_path(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    re_path(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),

]