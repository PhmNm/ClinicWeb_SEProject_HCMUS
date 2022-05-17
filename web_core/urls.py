from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urls_pattern = [
    path('', views.home, name='home'),
]
