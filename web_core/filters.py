from dataclasses import field
import django_filters 
from django_filters import CharFilter
from .models import *


class LichSuKhamFilter(django_filters.FilterSet):
    ID = CharFilter(field_name="id_benhnhan",lookup_expr='exact')
    class Meta:
        model = PHIEUKHAM
        fields = ''