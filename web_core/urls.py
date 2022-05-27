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

    path('thaydoi/loaibenh', views.thaydoi_loaibenh, name='quanli_thaydoi_loaibenh'),
    path('thaydoi/loaibenh/them', views.thaydoi_loaibenh_them, name='quanli_thaydoi_loaibenh_them'),
    path('thaydoi/loaibenh/xoa/<str:ten>', views.thaydoi_loaibenh_xoa, name='quanli_thaydoi_loaibenh_xoa'),

    path('thaydoi/donvitinh', views.thaydoi_dvt, name='quanli_thaydoi_dvt'),
    path('thaydoi/donvitinh/them', views.thaydoi_dvt_them, name='quanli_thaydoi_dvt_them'),
    path('thaydoi/donvitinh/xoa/<str:ten>', views.thaydoi_dvt_xoa, name='quanli_thaydoi_dvt_xoa'),

    path('thaydoi/cachdung', views.thaydoi_cachdung, name='quanli_thaydoi_cachdung'),
    path('thaydoi/cachdung/them', views.thaydoi_cachdung_them, name='quanli_thaydoi_cachdung_them'),
    path('thaydoi/cachdung/xoa/<str:ten>', views.thaydoi_cachdung_xoa, name='quanli_thaydoi_cachdung_xoa'),

    path('thaydoi/thuoc', views.thaydoi_thuoc, name='quanli_thaydoi_thuoc'),
    path('thaydoi/thuoc/them', views.thaydoi_thuoc_them, name='quanli_thaydoi_thuoc_them'),
    path('thaydoi/thuoc/xoa/<str:ten>', views.thaydoi_thuoc_xoa, name='quanli_thaydoi_thuoc_xoa'),
    path('thaydoi/thuoc/sua/<str:ten>', views.thaydoi_thuoc_sua, name='quanli_thaydoi_thuoc_sua'),
]
