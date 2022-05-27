from django.shortcuts import render, redirect

#models import
from .models import *

#authentication import
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, admin_only

#utils
from datetime import datetime as dt

#forms import
from .forms import benhnhan_form, phieukham_form
from django.forms import inlineformset_factory

#filters import
from .filters import dskb_filter

#authentication import
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, admin_only

#utils
from datetime import datetime as dt

#forms import
from .forms import benhnhan_form

#filter
from .filters import LichSuKhamFilter
# Create your views here.

##Authenticate User
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
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
    max_benhnhan = THAMSO.objects.get(loai='Số lượng bệnh nhân tối đa').now_value
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
    tienthuoc = 0
    for sdthuoc in sdthuocs:
        tienthuoc += sdthuoc.soluong * sdthuoc.thuoc.gia_tri
    context = {'phieukham':phieukham, 'tienkham':tienkham, 'tienthuoc':tienthuoc}
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
