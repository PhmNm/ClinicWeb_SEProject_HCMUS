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

#
def home(request):
    return render(request, 'web_core/dashboard.html')

@login_required(login_url='login')
def dskb(request):
    phieukhams = PHIEUKHAM.objects.filter(ngay_kham__date=dt.today().date())
    # phieukhams = PHIEUKHAM.objects.filter(ngay_kham__date=dt(2022,5,20))

    benhnhans = BENHNHAN.objects.filter(id__in=[bn.id_benhnhan.id for bn in phieukhams])
    count = len(benhnhans)
    max_benhnhan = THAMSO.objects.get(loai='Số lượng bệnh nhân tối đa').now_value
    today = dt.today().date().strftime('%d/%m/%Y')
    enum_dskb = enumerate(benhnhans,start = 1)
    context = {'enum_dskb':enum_dskb, 'count':count, 'max_benhnhan':max_benhnhan, 'today':today}
    return render(request, 'web_core/dskb.html', context)


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