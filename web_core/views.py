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
    phieukhams = PHIEUKHAM.objects.filter(ngay_kham__date=dt.today().date())
    benhnhans = BENHNHAN.objects.filter(id__in=[bn.id_benhnhan.id for bn in phieukhams])
    count = len(benhnhans)
    max_benhnhan = THAMSO.objects.get(loai='Số lượng bệnh nhân tối đa').now_value
    today = dt.today().date().strftime('%d/%m/%Y')
    enum_dskb = enumerate(benhnhans,start = 1)
    context = {'enum_dskb':enum_dskb, 'count':count, 'max_benhnhan':max_benhnhan, 'today':today}
    return render(request, 'web_core/dskb.html', context)

@admin_only
def dsbn(request):
    dsbn = BENHNHAN.objects.all()
    context = {'dsbn':dsbn}
    return render(request, 'web_core/dsbn.html', context)

@admin_only
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