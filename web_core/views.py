from django.shortcuts import render, redirect

# models import
from .models import *

# utils
from datetime import datetime as dt
from django.db.models import Count, Sum

# forms import
from .forms import ThayDoiGiaTriForm, DanhMucForm


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

    context = {'thang': thang, 'stt': stt, 'ngay': ngay, 'so_benh_nhan': so_benh_nhan, 'doanh_thu': doanh_thu,
               'ty_le': ty_le}
    return render(request, 'web_core/baocaodoanhthuthang.html', context=context)


def baocao_sudungthuoc(request):
    thang = dt.today().strftime('%m/%Y')
    queryset_ngay = PHIEUKHAM.objects.filter(ngay_kham__month=dt.today().date().month).values_list('id', flat=True)
    sdthuoc = SUDUNGTHUOC.objects.filter(id_phieukham__in=queryset_ngay)

    rows = (sdthuoc
            .values('thuoc', 'don_vi')
            .annotate(so_luong=Sum('soluong'))
            .annotate(so_lan_dung=Count('thuoc'))
            .order_by()
            )

    stt = [x for x in range(len(rows))]

    context = {'thang': thang, 'stt': stt, 'rows': rows}
    return render(request, 'web_core/baocaosudungthuoc.html', context=context)


def thaydoi_quydinh(request):
    return render(request, 'web_core/thaydoiquydinh.html')


def thaydoi_slbn(request):
    slbn = THAMSO.objects.get(loai='Số lượng bệnh nhân tối đa')
    now_val = THAMSO.objects.filter(loai='Số lượng bệnh nhân tối đa').values_list('now_value', flat=True)[0]
    form = ThayDoiGiaTriForm(initial={'loai': slbn, 'now_value': now_val})

    if request.method == 'POST':
        form = ThayDoiGiaTriForm(request.POST, instance=slbn)
        if form.is_valid():
            form.save()
            return redirect('/thaydoi')

    context = {'form': form}
    return render(request, 'web_core/thaydoi_slbn.html', context)


def thaydoi_tienkham(request):
    tien_kham = THAMSO.objects.get(loai='Tiền khám')
    now_val = THAMSO.objects.filter(loai='Tiền khám').values_list('now_value', flat=True)[0]
    form = ThayDoiGiaTriForm(initial={'loai': tien_kham, 'now_value': now_val})

    if request.method == 'POST':
        form = ThayDoiGiaTriForm(request.POST, instance=tien_kham)
        if form.is_valid():
            form.save()
            return redirect('/thaydoi')

    context = {'form': form}
    return render(request, 'web_core/thaydoi_tienkham.html', context)


def thaydoi_loaibenh(request):
    dslb = DANHMUC.objects.filter(loai='Bệnh').values_list('ten', flat=True)
    context = {'dslb': dslb}
    return render(request, 'web_core/thaydoi_loaibenh.html', context)


def thaydoi_loaibenh_them(request):
    benh = DANHMUC(loai='Bệnh')
    form = DanhMucForm()

    if request.method == 'POST':
        form = DanhMucForm(request.POST, instance=benh)
        if form.is_valid():
            form.save()
            return redirect('/thaydoi/loaibenh')

    context = {'form': form}
    return render(request, 'web_core/thaydoi_loaibenh_them.html', context)


def thaydoi_loaibenh_xoa(request, ten):
    benh = DANHMUC.objects.get(ten=ten)

    if request.method == 'POST':
        benh.delete()
        return redirect('/thaydoi/loaibenh')

    context = {'benh': benh}
    return render(request, 'web_core/thaydoi_loaibenh_xoa.html', context)


def thaydoi_dvt(request):
    dsdvt = DANHMUC.objects.filter(loai='Đơn vị').values_list('ten', flat=True)
    context = {'dsdvt': dsdvt}
    return render(request, 'web_core/thaydoi_dvt.html', context)


def thaydoi_dvt_them(request):
    dvt = DANHMUC(loai='Đơn vị')
    form = DanhMucForm()

    if request.method == 'POST':
        form = DanhMucForm(request.POST, instance=dvt)
        if form.is_valid():
            form.save()
            return redirect('/thaydoi/donvitinh')

    context = {'form': form}
    return render(request, 'web_core/thaydoi_dvt_them.html', context)


def thaydoi_dvt_xoa(request, ten):
    dvt = DANHMUC.objects.get(ten=ten)

    if request.method == 'POST':
        dvt.delete()
        return redirect('/thaydoi/donvitinh')

    context = {'dvt': dvt}
    return render(request, 'web_core/thaydoi_dvt_xoa.html', context)


def thaydoi_cachdung(request):
    ds_cach_dung = DANHMUC.objects.filter(loai='Cách dùng').values_list('ten', flat=True)
    context = {'ds_cach_dung': ds_cach_dung}
    return render(request, 'web_core/thaydoi_cachdung.html', context)


def thaydoi_cachdung_them(request):
    cach_dung = DANHMUC(loai='Cách dùng')
    form = DanhMucForm()

    if request.method == 'POST':
        form = DanhMucForm(request.POST, instance=cach_dung)
        if form.is_valid():
            form.save()
            return redirect('/thaydoi/cachdung')

    context = {'form': form}
    return render(request, 'web_core/thaydoi_cachdung_them.html', context)


def thaydoi_cachdung_xoa(request, ten):
    cach_dung = DANHMUC.objects.get(ten=ten)

    if request.method == 'POST':
        cach_dung.delete()
        return redirect('/thaydoi/cachdung')

    context = {'cach_dung': cach_dung}
    return render(request, 'web_core/thaydoi_cachdung_xoa.html', context)
