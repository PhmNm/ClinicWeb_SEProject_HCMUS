from django.forms import ModelForm, DateInput, ValidationError, DateField
from .models import *


class ThayDoiGiaTriForm(ModelForm):
    class Meta:
        model = THAMSO
        fields = ['now_value']
