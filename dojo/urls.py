#dojo/urls.py
from django.urls import path, re_path

from dojo import views
from . import views_cbv

app_name = 'dojo'

urlpatterns = [
    path('new/', views.post_new),
    re_path(r'^(?P<id>\d+)/edit/$', views.post_edit),

    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum, name='mysum'),
    re_path(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello, name='hello'),
    path('list1/', views.post_list1, name='post_list1'),
    path('list2/', views.post_list2, name='post_list2'),
    path('list3/', views.post_list3, name='post_list3'),
    path('excel/', views.excel_download, name='excel_download'),

    path('cbv/list1/', views_cbv.post_list1, name='post_list1'),
    path('cbv/list2/', views_cbv.post_list2, name='post_list2'),
    path('cbv/list3/', views_cbv.post_list3, name='post_list3'),
    path('cbv/excel/', views_cbv.excel_download, name='excel_download'),
]