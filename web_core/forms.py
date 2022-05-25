from django.forms import ModelForm, DateInput, ValidationError, DateField
from .models import *

class benhnhan_form(ModelForm):
    ngay_sinh = DateField(
        widget=DateInput(format='%d/%m/%Y'),
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