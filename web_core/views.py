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
from .forms import benhnhan_form

#filters import
from .filters import dskb_filter

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

#
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
