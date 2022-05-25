from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('dskb', views.dskb, name='quanli_dskb'),
    path('dspk',views.dspk, name='quanli_dspk'),
    path('them_pk', views.add_phieukham, name='quanli_them_phieukham'),
    path('sua_pk/<str:id>', views.edit_phieukham, name='quanli_sua_phieukham'),
    path('xoa_pk/<str:id>', views.del_phieukham, name='quanli_xoa_phieukham'),
]
