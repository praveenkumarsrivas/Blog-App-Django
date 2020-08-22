from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("contact", views.contact, name="contact"),
    path("writeblog", views.writeblog, name="writeblog"),
    path("read", views.read, name="read"),
    path("search", views.search, name="search"),
    # path('<str:blogtopic>', views.post, name="post"),
    # path('upload', views.upload_image),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
