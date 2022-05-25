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
    context = {}
    return render(request, 'web_core/baocaodoanhthuthang.html', context=context)


def baocao_sudungthuoc(request):
    context = {}
    return render(request, 'web_core/baocaosudungthuoc.html', context=context)
