from django.forms import DateField, Form, DateInput, ValidationError
from datetime import datetime as dt
from django_filters import CharFilter, FilterSet
from .models import *

class dskb_filter(Form):
    ngay_kham = DateField(
        initial=dt.today().date(),
        required=False,
        label='Ngày khám',
        input_formats=["%d/%m/%Y"],
        widget=DateInput(format="%d/%m/%Y"),
        label_suffix=' (Định dạng nhập: "dd/mm/YYYY")',
        error_messages={'invalid':'Yêu cầu nhập đúng định dạng'},
    )

class baocao_filter(Form):
    thang_bao_cao = DateField(
        initial=dt.today().date().strftime('%m/%Y'),
        required=False,
        label='Lập báo cáo tháng: ',
        input_formats=["%m/%Y"],
        widget=DateInput(format="%m/%Y"),
        label_suffix=' (Định dạng nhập: "mm/YYYY")',
        error_messages={'invalid': 'Yêu cầu nhập đúng định dạng'},
    )

class LichSuKhamFilter(FilterSet):
    ID = CharFilter(field_name="id_benhnhan",lookup_expr='exact', strip=False)
    class Meta:
        model = PHIEUKHAM
        fields = ''
