from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('dskb', views.dskb, name='quanli_dskb'),
    path('dsbn', views.dsbn, name='quanli_dsbn'),
    path('them_bn', views.add_benhnhan, name='quanli_them_benhnhan'),
    path('sua_bn/<str:id>', views.edit_benhnhan, name='quanli_sua_benhnhan'),
    path('xoa_bn/<str:id>', views.del_benhnhan, name='quanli_xoa_benhnhan'),
    path('xuathoadon', views.xuathoadon, name='quanli_xuathoadon'),
    path('hoadon/<str:pk>/', views.hoadon, name='quanli_xuathoadon_hoadon'),
    path('lsk',views.lsk, name='quanli_lsk'),
    path('lsk_guest',views.lsk_guest, name='lsk_guest'),
]
