from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('lapbaocao/', views.lap_bao_cao, name='quanli_lapbaocao'),
    path('lapbaocao/doanhthuthang/', views.baocao_doanhthuthang, name='quanli_lapbaocao_bcdtt'),
    path('lapbaocao/sudungthuoc/', views.baocao_sudungthuoc, name='quanli_lapbaocao_bcsdt'),
    path('thaydoi/', views.thaydoi_quydinh, name='quanli_thaydoi'),
    path('thaydoi/soluongbenhnhan', views.thaydoi_slbn, name='quanli_thaydoi_slbn'),
    path('thaydoi/tienkham', views.thaydoi_tienkham, name='quanli_thaydoi_tienkham'),
]
