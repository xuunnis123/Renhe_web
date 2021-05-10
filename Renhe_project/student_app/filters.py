from .models import Case
import django_filters
from django import forms
class CaseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name',lookup_expr='icontains', label="個案學生姓名查詢",widget=forms.TextInput(attrs={'class': 'form-control'}))
    '''
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    '''
    '''
    school = django_filters.CharFilter(
        widget=forms.Select(choices=(('', '請選擇'),) + Movie.GENRE_CHOICES, attrs={'class': 'form-control'}))

    start_date = django_filters.CharFilter(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))

    end_date
    '''
    class Meta:
        model = Case
        fields = ['name',]