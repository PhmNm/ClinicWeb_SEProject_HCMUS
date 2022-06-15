from django.shortcuts import render, redirect

#models import
from .models import *

#authentication import
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required
from .decorators import admin_only

#utils
from datetime import datetime as dt
from django.db.models import Count, Sum, F

#forms import
from .forms import benhnhan_form, phieukham_form, ThayDoiGiaTriForm, DanhMucForm, ThuocForm
from django.forms import inlineformset_factory

#filters import
from .filters import dskb_filter, baocao_filter, LichSuKhamFilter

# Create your views here.

##Authenticate User
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dskb')
        else:
            messages.info(request,'Username Or Password was incorrect')
    context = {}
    return render(request, 'web_core/login.html', context)
def logoutUser(request):
    logout(request)
    return redirect('login')

##Functions
def home(request):
    return render(request, 'web_core/dashboard.html')

@login_required(login_url='login')
def dskb(request):
    if len(THAMSO.objects.filter(loai='Số lượng bệnh nhân tối đa')) != 0:
        max_benhnhan = THAMSO.objects.get(loai='Số lượng bệnh nhân tối đa').now_value
    else: max_benhnhan = 40
    today = dt.today().date()
    form = dskb_filter
    if request.method == 'POST':
        form = dskb_filter(request.POST)
        if form.is_valid() and form['ngay_kham'].data != "":
            today = dt.strptime(form['ngay_kham'].data,'%d/%m/%Y')
    phieukhams = PHIEUKHAM.objects.filter(ngay_kham__date=today)
    benhnhans = []
    for benhnhan in phieukhams:
        benhnhans.append(BENHNHAN.objects.get(id=benhnhan.id_benhnhan.id))
    count = len(phieukhams)
    enum_dskb = enumerate(benhnhans,start = 1)
    context = {'enum_dskb':enum_dskb, 'count':count, 'max_benhnhan':max_benhnhan, 'today':today.strftime('%d/%m/%Y'), 'form': form}
    return render(request, 'web_core/dskb.html', context)

@admin_only
def dsbn(request):
    dsbn = BENHNHAN.objects.all()
    context = {'dsbn':dsbn}
    return render(request, 'web_core/dsbn.html', context)

def add_benhnhan(request):
    form = benhnhan_form()
    if request.method == 'POST':
        form = benhnhan_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dskb')
    context = {'form':form}
    return render(request,'web_core/add_benhnhan.html', context)

@admin_only
def edit_benhnhan(request, id):
    benhnhan = BENHNHAN.objects.get(id=id)
    form = benhnhan_form(instance=benhnhan)
    if request.method == 'POST':
        form = benhnhan_form(request.POST, instance=benhnhan)
        if form.is_valid():
            form.save()
            return redirect('/dsbn')
    context = {'form':form}
    return render(request,'web_core/edit_benhnhan.html', context)

@admin_only
def del_benhnhan(request, id):
    benhnhan = BENHNHAN.objects.get(id=id)
    if request.method == 'POST':
        benhnhan.delete()
        return redirect('/dsbn')
    context = {'benhnhan':benhnhan}
    return render(request,'web_core/del_benhnhan.html', context)

@login_required(login_url='login')
def xuathoadon(request):
    phieukhams = PHIEUKHAM.objects.all()
    enum_xhd = enumerate(phieukhams,start = 1)
    context = {'phieukhams':phieukhams, 'enum_xhd':enum_xhd}
    return render(request, 'web_core/xuathoadon.html', context)

@login_required(login_url='login')
def hoadon(request, pk):
    phieukham = PHIEUKHAM.objects.get(id=pk)
    tienkham = THAMSO.objects.get(loai='Tiền khám').now_value
    sdthuocs = SUDUNGTHUOC.objects.filter(id_phieukham=phieukham)  
    enum_dsthuoc = enumerate(sdthuocs,start = 1) 
    tienthuoc = 0
    for sdthuoc in sdthuocs:
        tienthuoc += sdthuoc.soluong * sdthuoc.thuoc.gia_tri
    tong = tienkham + tienthuoc
    context = {'phieukham':phieukham, 'tienkham':tienkham, 'tienthuoc':tienthuoc, 'tongtien':tong, 'enum_dsthuoc':enum_dsthuoc}
    return render(request, 'web_core/hoadon.html', context)

@login_required(login_url='login')
def lsk(request):
    lsk = PHIEUKHAM.objects.all().order_by('ngay_kham')
    enum_lsk = enumerate(lsk, start = 1)
    myFilter = LichSuKhamFilter()
    if request.GET.__contains__('ID'):
        myFilter = LichSuKhamFilter(request.GET,queryset=lsk)
        lsk = myFilter.qs
        enum_lsk = enumerate(lsk, start = 1)

    context ={'lsk': lsk, 'myFilter':myFilter, 'enum_lsk': enum_lsk}
    return render(request, 'web_core/lsk.html',context)

def lsk_guest(request):
    lsk_guest = None
    myFilter = LichSuKhamFilter()
    enum_lsk_guest = None
    if request.method == 'GET' and 'ID' in request.GET:
        ID = request.GET['ID']
        if ID :
            lsk_guest = PHIEUKHAM.objects.all().order_by('ngay_kham')
            myFilter = LichSuKhamFilter(request.GET,queryset=lsk_guest)
            lsk_guest = myFilter.qs
            enum_lsk_guest = enumerate(lsk_guest, start = 1)
        else:
            lsk_guest = None
        
    context ={'lsk_guest': lsk_guest, 'myFilter':myFilter,'enum_lsk_guest':enum_lsk_guest}
    return render(request, 'web_core/lsk_guest.html',context)
@login_required(login_url='login')
def dspk(request):
    dspk = PHIEUKHAM.objects.all().order_by('-ngay_kham')
    enum_dspk = enumerate(dspk,start = 1)

    context = {'enum_dspk':enum_dspk}
    return render(request, 'web_core/dspk.html', context)

@login_required(login_url='login')
def view_phieukham(request, id):
    phieukham = PHIEUKHAM.objects.get(id=id)
    sdt = SUDUNGTHUOC.objects.filter(id_phieukham = id)
    enum_dsthuoc = enumerate(sdt,start = 1)
    context = {'phieukham':phieukham, 'enum_dsthuoc':enum_dsthuoc}
    return render(request,'web_core/view_phieukham.html', context)

@login_required(login_url='login')
def add_phieukham(request):
    sdtFormSet = inlineformset_factory(PHIEUKHAM, SUDUNGTHUOC, 
                 fields=('id_phieukham','thuoc', 'soluong', 'don_vi', 'cach_dung'), extra=10)
    pk_form = phieukham_form()
    formset = sdtFormSet()
    if request.method == 'POST':
        print(request.POST)
        pk_form = phieukham_form(request.POST)
        if pk_form.is_valid():
            pk_form.save()
        pk = PHIEUKHAM.objects.get(id = pk_form['id'].data)
        formset = sdtFormSet(request.POST, instance=pk)
        if formset.is_valid():
            formset.save()
            return redirect('/dspk')
    context = {'pk_form':pk_form, 'formset':formset}
    return render(request,'web_core/add_phieukham.html', context)

@admin_only
def edit_phieukham(request, id):
    sdtFormSet = inlineformset_factory(PHIEUKHAM, SUDUNGTHUOC, 
                 fields=('id_phieukham','thuoc', 'soluong', 'don_vi', 'cach_dung'), extra=10)
    phieukham = PHIEUKHAM.objects.get(id=id)
    pk_form = phieukham_form(instance=phieukham)
    formset = sdtFormSet(instance=phieukham)
    if request.method == 'POST':
        pk_form = phieukham_form(request.POST, instance=phieukham)
        if pk_form.is_valid():
            pk_form.save()
        formset = sdtFormSet(request.POST, instance=phieukham)
        if formset.is_valid():
            formset.save()
            return redirect('/dspk')
    context = {'pk_form':pk_form, 'formset':formset}
    return render(request,'web_core/edit_phieukham.html', context)

@admin_only
def del_phieukham(request, id):
    phieukham = PHIEUKHAM.objects.get(id=id)
    if request.method == 'POST':
        phieukham.delete()
        return redirect('/dspk')
    context = {'phieukham':phieukham}
    return render(request,'web_core/del_phieukham.html', context)

@admin_only
def lap_bao_cao(request):
    return render(request, 'web_core/lapbaocao.html')

@admin_only
def baocao_doanhthuthang(request):
    thang_nam = dt.today().date()
    form = baocao_filter
    if request.method == 'POST':
        form = baocao_filter(request.POST)
        if form.is_valid() and form['thang_bao_cao'].data != "":
            thang_nam = dt.strptime(form['thang_bao_cao'].data, '%m/%Y')

    queryset_dict_ngay = PHIEUKHAM.objects.values('ngay_kham').filter(ngay_kham__month=thang_nam.month).filter(ngay_kham__year=thang_nam.year)
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

    context = {'thang': thang_nam.strftime('%m/%Y'), 'stt': stt, 'ngay': ngay, 'so_benh_nhan': so_benh_nhan, 'doanh_thu': doanh_thu,
               'ty_le': ty_le, 'form': form}
    return render(request, 'web_core/baocaodoanhthuthang.html', context=context)

@admin_only
def baocao_sudungthuoc(request):
    thang_nam = dt.today().date()
    form = baocao_filter
    if request.method == 'POST':
        form = baocao_filter(request.POST)
        if form.is_valid() and form['thang_bao_cao'].data != "":
            thang_nam = dt.strptime(form['thang_bao_cao'].data, '%m/%Y')

    queryset_ngay = PHIEUKHAM.objects.filter(ngay_kham__month=thang_nam.month).filter(ngay_kham__year=thang_nam.year).values_list('id', flat=True)
    sdthuoc = SUDUNGTHUOC.objects.filter(id_phieukham__in=queryset_ngay)

    rows = (sdthuoc
            .values('thuoc', 'don_vi')
            .annotate(ten_thuoc = F('thuoc__ten'))
            .annotate(ten_donvi = F('don_vi__ten'))
            .annotate(so_luong=Sum('soluong'))
            .annotate(so_lan_dung=Count('thuoc'))
            .order_by()
            )

    stt = [x for x in range(len(rows))]
    context = {'thang': thang_nam.strftime('%m/%Y'), 'stt': stt, 'rows': rows, 'form': form}
    return render(request, 'web_core/baocaosudungthuoc.html', context=context)

@admin_only
def thaydoi_quydinh(request):
    return render(request, 'web_core/thaydoiquydinh.html')

@admin_only
def thaydoi_slbn(request):
    slbn = THAMSO.objects.get(loai='Số lượng bệnh nhân tối đa')
    form = ThayDoiGiaTriForm(initial={'loai': slbn, 'now_value': slbn.now_value})

    if request.method == 'POST':
        form = ThayDoiGiaTriForm(request.POST, instance=slbn)
        if form.is_valid():
            form.save()
            return redirect('/thaydoi')

    context = {'form': form}
    return render(request, 'web_core/thaydoi_slbn.html', context)

@admin_only
def thaydoi_tienkham(request):
    tien_kham = THAMSO.objects.get(loai='Tiền khám')
    form = ThayDoiGiaTriForm(initial={'loai': tien_kham, 'now_value': tien_kham.now_value})

    if request.method == 'POST':
        form = ThayDoiGiaTriForm(request.POST, instance=tien_kham)
        if form.is_valid():
            form.save()
            return redirect('/thaydoi')

    context = {'form': form}
    return render(request, 'web_core/thaydoi_tienkham.html', context)

@admin_only
def thaydoi_loaibenh(request):
    dslb = DANHMUC.objects.filter(loai='Bệnh')
    context = {'dslb': dslb}
    return render(request, 'web_core/thaydoi_loaibenh.html', context)

@admin_only
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

@admin_only
def thaydoi_loaibenh_xoa(request, id):
    benh = DANHMUC.objects.get(id=id)

    if request.method == 'POST':
        benh.delete()
        return redirect('/thaydoi/loaibenh')

    context = {'benh': benh}
    return render(request, 'web_core/thaydoi_loaibenh_xoa.html', context)

@admin_only
def thaydoi_dvt(request):
    dsdvt = DANHMUC.objects.filter(loai='Đơn vị')
    context = {'dsdvt': dsdvt}
    return render(request, 'web_core/thaydoi_dvt.html', context)

@admin_only
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

@admin_only
def thaydoi_dvt_xoa(request, id):
    dvt = DANHMUC.objects.get(id=id)

    if request.method == 'POST':
        dvt.delete()
        return redirect('/thaydoi/donvitinh')

    context = {'dvt': dvt}
    return render(request, 'web_core/thaydoi_dvt_xoa.html', context)

@admin_only
def thaydoi_cachdung(request):
    ds_cach_dung = DANHMUC.objects.filter(loai='Cách dùng')
    context = {'ds_cach_dung': ds_cach_dung}
    return render(request, 'web_core/thaydoi_cachdung.html', context)

@admin_only
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

@admin_only
def thaydoi_cachdung_xoa(request, id):
    cach_dung = DANHMUC.objects.get(id=id)

    if request.method == 'POST':
        cach_dung.delete()
        return redirect('/thaydoi/cachdung')

    context = {'cach_dung': cach_dung}
    return render(request, 'web_core/thaydoi_cachdung_xoa.html', context)

@admin_only
def thaydoi_thuoc(request):
    ds_thuoc = DANHMUC.objects.filter(loai='Thuốc')
    context = {'ds_thuoc': ds_thuoc}
    return render(request, 'web_core/thaydoi_thuoc.html', context)

@admin_only
def thaydoi_thuoc_them(request):
    thuoc = DANHMUC(loai='Thuốc')
    form = ThuocForm()

    if request.method == 'POST':
        form = ThuocForm(request.POST, instance=thuoc)
        if form.is_valid():
            form.save()
            return redirect('/thaydoi/thuoc')

    context = {'form': form}
    return render(request, 'web_core/thaydoi_thuoc_them.html', context)

@admin_only
def thaydoi_thuoc_xoa(request, id):
    thuoc = DANHMUC.objects.get(id=id)

    if request.method == 'POST':
        thuoc.delete()
        return redirect('/thaydoi/thuoc')

    context = {'thuoc': thuoc}
    return render(request, 'web_core/thaydoi_thuoc_xoa.html', context)

@admin_only
def thaydoi_thuoc_sua(request, id):
    thuoc = DANHMUC.objects.get(id=id)
    form = ThuocForm(instance=thuoc, initial={'ten': thuoc.ten, 'gia_tri': thuoc.gia_tri})

    if request.method == 'POST':
        form = ThuocForm(request.POST, instance=thuoc)
        if form.is_valid():
            form.save()
            return redirect('/thaydoi/thuoc')

    context = {'ten_thuoc': thuoc.ten, 'form': form}
    return render(request, 'web_core/thaydoi_thuoc_sua.html', context)