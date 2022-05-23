from django.shortcuts import render, redirect

#models import
from .models import *

#authentication import
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users

#utils
from datetime import datetime as dt

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
    context = {'benhnhans':benhnhans, 'count':count, 'max_benhnhan':max_benhnhan}
    return render(request, 'web_core/dskb.html', context)

@login_required(login_url='login')
def xuathoadon(request):
    phieukhams = PHIEUKHAM.objects.all()
    enum_xhd = enumerate(phieukhams,start = 1)
    context = {'phieukhams':phieukhams, 'enum_xhd':enum_xhd}
    return render(request, 'web_core/xuathoadon.html', context)