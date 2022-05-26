from dataclasses import fields
from django.forms import ModelForm
from .models import *

class phieukham_form(ModelForm):
    class Meta:
        model = PHIEUKHAM
        fields = '__all__'

class sudungthuoc_form(ModelForm):
    class Meta:
        model = SUDUNGTHUOC
        fields = '__all__'