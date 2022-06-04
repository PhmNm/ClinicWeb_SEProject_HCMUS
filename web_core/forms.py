from django.forms import ModelForm, DateInput, ValidationError, DateField
from .models import *

class benhnhan_form(ModelForm):
    ngay_sinh = DateField(
        label='Ngày sinh',
        widget=DateInput(format="%d/%m/%Y"),
        input_formats=['%d/%m/%Y']
    )
    class Meta:
        model = BENHNHAN
        fields = '__all__'
        widgets = {
            'ngay_sinh': DateInput(format="%d/%m/%Y"),
        }
    def clean(self):
        benhnhan = BENHNHAN.objects.filter(
            ho_ten=self.cleaned_data.get("ho_ten"),
            ngay_sinh=self.cleaned_data.get("ngay_sinh"),
            gioi_tinh=self.cleaned_data.get("gioi_tinh"),
            dia_chi=self.cleaned_data.get("dia_chi"),
            )
        if benhnhan.exists():
            raise ValidationError("Bệnh nhân đã tồn tại")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["id"].widget.attrs["readonly"] = True

class phieukham_form(ModelForm):
    class Meta:
        model = PHIEUKHAM
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["id"].widget.attrs["readonly"] = True

class sudungthuoc_form(ModelForm):
    class Meta:
        model = SUDUNGTHUOC
        fields = '__all__'

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
