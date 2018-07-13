from django.contrib import admin
from django.urls import path, include, re_path
from shufic import shufic_url
from login import login_url
urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'^videoshufic/', include(shufic_url)),
    re_path(r'^auth/', include(login_url)),
]