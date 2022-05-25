from django.shortcuts import render, redirect

# models import
from .models import *

# utils
from datetime import datetime as dt

# forms import
# from .forms import benhnhan_form


# Create your views here.
def home(request):
    return render(request, 'web_core/dashboard.html')


def lap_bao_cao(request):
    return render(request, 'web_core/lapbaocao.html')


def baocao_doanhthuthang(request):
    thang = dt.today().strftime('%m/%Y')
    queryset_dict_ngay = PHIEUKHAM.objects.values('ngay_kham').filter(ngay_kham__month=dt.today().date().month)

    ngay = []
    so_benh_nhan = []
    doanh_thu = []

    for dict_ngay in queryset_dict_ngay:
        # print(dict_ngay['ngay_kham'].strftime('%d/%m/%Y'))
        ngay_kham = dict_ngay['ngay_kham'].date()
        if len(ngay) > 0 and ngay_kham == ngay[-1]:
            continue

        ngay.append(ngay_kham)
        phieukham_ngay = PHIEUKHAM.objects.filter(ngay_kham__date=ngay_kham)
        so_benh_nhan.append(phieukham_ngay.count())
        doanh_thu_ngay = 0

        for phieu in phieukham_ngay:
            sdthuocs = SUDUNGTHUOC.objects.filter(id_phieukham=phieu.id)
            print(sdthuocs)
            for sdthuoc in sdthuocs:
                doanh_thu_ngay += sdthuoc.soluong * sdthuoc.thuoc.gia_tri

        doanh_thu_ngay += so_benh_nhan[-1] * THAMSO.objects.get(loai='Tiền khám').now_value
        doanh_thu.append(doanh_thu_ngay)

    ty_le = [round(100 * x / sum(doanh_thu), 2) for x in doanh_thu]
    stt = [x for x in range(len(ngay))]

    context = {'thang': thang, 'stt': stt, 'ngay': ngay, 'so_benh_nhan': so_benh_nhan, 'doanh_thu': doanh_thu, 'ty_le': ty_le}
    return render(request, 'web_core/baocaodoanhthuthang.html', context=context)


def baocao_sudungthuoc(request):
    context = {}
    return render(request, 'web_core/baocaosudungthuoc.html', context=context)
