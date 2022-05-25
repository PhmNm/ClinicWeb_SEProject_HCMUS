from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('dskb', views.dskb, name='quanli_dskb'),
    path('dsbn', views.dsbn, name='quanli_dsbn'),
    path('dspk',views.dspk, name='quanli_dspk'),
]
