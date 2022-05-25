from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('lapbaocao', views.lap_bao_cao, name='quanli_lapbaocao'),
    path('lapbaocao/doanhthuthang', views.baocao_doanhthuthang, name='quanli_lapbaocao_bcdtt'),
    path('lapbaocao/sudungthuoc', views.baocao_sudungthuoc, name='quanli_lapbaocao_bcsdt'),
]
