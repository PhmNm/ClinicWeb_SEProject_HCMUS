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

    path('dspk',views.dspk, name='quanli_dspk'),
    path('xem_pk/<str:id>', views.view_phieukham, name='quanli_xem_phieukham'),
    path('them_pk', views.add_phieukham, name='quanli_them_phieukham'),
    path('sua_pk/<str:id>', views.edit_phieukham, name='quanli_sua_phieukham'),
    path('xoa_pk/<str:id>', views.del_phieukham, name='quanli_xoa_phieukham'),

    path('lapbaocao/', views.lap_bao_cao, name='quanli_lapbaocao'),
    path('lapbaocao/doanhthuthang/', views.baocao_doanhthuthang, name='quanli_lapbaocao_bcdtt'),
    path('lapbaocao/sudungthuoc/', views.baocao_sudungthuoc, name='quanli_lapbaocao_bcsdt'),

    path('thaydoi/', views.thaydoi_quydinh, name='quanli_thaydoi'),
    path('thaydoi/soluongbenhnhan', views.thaydoi_slbn, name='quanli_thaydoi_slbn'),
    path('thaydoi/tienkham', views.thaydoi_tienkham, name='quanli_thaydoi_tienkham'),

    path('thaydoi/loaibenh', views.thaydoi_loaibenh, name='quanli_thaydoi_loaibenh'),
    path('thaydoi/loaibenh/them', views.thaydoi_loaibenh_them, name='quanli_thaydoi_loaibenh_them'),
    path('thaydoi/loaibenh/xoa/<str:id>', views.thaydoi_loaibenh_xoa, name='quanli_thaydoi_loaibenh_xoa'),

    path('thaydoi/donvitinh', views.thaydoi_dvt, name='quanli_thaydoi_dvt'),
    path('thaydoi/donvitinh/them', views.thaydoi_dvt_them, name='quanli_thaydoi_dvt_them'),
    path('thaydoi/donvitinh/xoa/<str:id>', views.thaydoi_dvt_xoa, name='quanli_thaydoi_dvt_xoa'),

    path('thaydoi/cachdung', views.thaydoi_cachdung, name='quanli_thaydoi_cachdung'),
    path('thaydoi/cachdung/them', views.thaydoi_cachdung_them, name='quanli_thaydoi_cachdung_them'),
    path('thaydoi/cachdung/xoa/<str:id>', views.thaydoi_cachdung_xoa, name='quanli_thaydoi_cachdung_xoa'),

    path('thaydoi/thuoc', views.thaydoi_thuoc, name='quanli_thaydoi_thuoc'),
    path('thaydoi/thuoc/them', views.thaydoi_thuoc_them, name='quanli_thaydoi_thuoc_them'),
    path('thaydoi/thuoc/xoa/<str:id>', views.thaydoi_thuoc_xoa, name='quanli_thaydoi_thuoc_xoa'),
    path('thaydoi/thuoc/sua/<str:id>', views.thaydoi_thuoc_sua, name='quanli_thaydoi_thuoc_sua'),
]
