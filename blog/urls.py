#blog/urls.py
from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    re_path(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
]