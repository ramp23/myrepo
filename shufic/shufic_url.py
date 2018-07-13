from django.contrib import admin
from django.urls import path, include, re_path
from shufic import views
from shufic.views import addlikes, onevideo, addcomment, Hello
urlpatterns = [
    re_path(r'^$', views.Hello),
    re_path(r'^addlikes/(?P<video_id>\d+)/$', addlikes),
    re_path(r'^Vaddlikes/(?P<video_id>\d+)/$', addlikes),
    re_path(r'^onevideo/(?P<video_id>\d+)/$', onevideo),
    re_path(r'^addcomment/(?P<video_id>\d+)/$', addcomment),
]