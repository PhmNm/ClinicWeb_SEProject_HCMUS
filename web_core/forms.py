from django.forms import ModelForm, DateInput, ValidationError
from .models import *
from shortuuid.django_fields import ShortUUIDField

class benhnhan_form(ModelForm):
    class Meta:
        model = BENHNHAN
        fields = '__all__'
        widgets = {
            'ngay_sinh': DateInput(format='%d/%m/%Y'),
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