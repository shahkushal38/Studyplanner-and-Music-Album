from django.urls import path
from django.conf.urls import url
from . import views

app_name='studyplanner'
urlpatterns=[
    #/studyplanner/index/
    path('index',views.index, name='index'),

    #path('monday',views.monday),
    #path('tuesday',views.tuesday)
    path('<day>',views.weekly_timetable),

    #/studyplanner/712/
    url(r'^(?P<album_id>[0-9]+)/$',views.detail, name='detail'),

    #/studyplanner/album_id/favourite
    url(r'^(?P<album_id>[0-9]+)/favourite/$',views.favourite, name='favourite'),
    
    #/studyplanner/IndexView/
    url(r'^$',views.IndexView.as_view(),name='IndexView'),

    #/studyplanner/album/add/
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    #/studyplanner/album/album_id/update/
    url(r'album/(?P<pk>[0-9]+)/update/$', views.AlbumUpdate.as_view(), name='album-update'),

    #/studyplanner/album/album_id/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),


]