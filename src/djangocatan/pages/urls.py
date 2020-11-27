from django.urls import path, url
from django.contrib import admin

from . import views

url_patterns = [
    path('', views.home_view, name="home"),
]