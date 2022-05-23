from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('dskb', views.dskb, name='quanli_dskb'),
    path('xuathoadon', views.xuathoadon, name='quanli_xuathoadon'),
]
