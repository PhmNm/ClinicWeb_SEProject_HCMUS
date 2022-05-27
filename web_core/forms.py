from django.forms import ModelForm, DateInput, ValidationError, DateField
from .models import *


class ThayDoiGiaTriForm(ModelForm):
    class Meta:
        model = THAMSO
        fields = ['now_value']


class DanhMucForm(ModelForm):
    class Meta:
        model = DANHMUC
        fields = ['ten']


class ThuocForm(ModelForm):
    class Meta:
        model = DANHMUC
        fields = ['ten', 'gia_tri']
