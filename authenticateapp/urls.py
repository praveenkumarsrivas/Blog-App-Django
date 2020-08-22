from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views
import BlogApp
from django.shortcuts import render, redirect

urlpatterns = [
    path("", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("userlogin", views.userlogin, name="userlogin"),
    path("userlogout", views.userlogout, name="userlogout"),
    path("writeblog", BlogApp.views.writeblog, name="writeblog"),
    path("about", BlogApp.views.about, name="about"),
    path("read", BlogApp.views.read, name="read"),
    path("search", BlogApp.views.search, name="search"),
    path("base", views.search, name="base"),
]
