from django import forms
from django.forms import ModelForm, DateInput, ValidationError, DateField
from .models import *


class ThayDoiSlbnForm(ModelForm):
    class Meta:
        model = THAMSO
        # initial = {'loai': 'Số lượng bệnh nhân tối đa'}
        fields = ['now_value']
