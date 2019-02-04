#blog/urls.py
from . import views, views_cbv
from django.urls import path, re_path

app_name = 'blog'

urlpatterns = [
    path('', views_cbv.post_list, name='post_list'),
    re_path(r'^(?P<pk>\d+)/$', views_cbv.post_detail, name='post_detail'),

    path('new/', views.post_new, name='post_new'),
    re_path(r'^(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),

    path('cbv/new/', views_cbv.post_new),
]