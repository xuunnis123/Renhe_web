from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from . import models
from .filters import CaseFilter
import requests
from .models import Case
class CaseListView(ListView):
    print("CaseView")
    context_object_name='case'
    model= models.Case
    template_name='case_app/case_list.html'

class CaseDetailView(DetailView):
    
    context_object_name='case_detail'
    model=models.Case
    template_name='case_app/case_detail.html'


class CaseCreateView(CreateView):
    fields=('name','phone','school','contribute_context','is_scholorship','scholorship_amount','total_money','situation','visited_form','visited_photos','start_date','end_date')
    model=models.Case
    success_url= reverse_lazy("case_app:list")
class CaseUpdateView(UpdateView):
    fields=('phone','school','contribute_context','is_scholorship','scholorship_amount','total_money','situation','visited_form','visited_photos','start_date','end_date')
    model=models.Case
    success_url= reverse_lazy("case_app:list")
class CaseDeleteView(DeleteView):
    model=models.Case
    success_url= reverse_lazy("case_app:list")

def add_amount(is_scholorship):
    if is_scholorship==True:
        scholorship_amount='enable'
        #add amount 
        return True
    else: return False

def case_filter(request):
    cases = Case.objects.all()
    f = CaseFilter(request.GET, queryset=Case.objects.filter(name='p'))
    context = {'filter': f, }

    '''
    caseFilter = CaseFilter(queryset=cases)

    if request.method == "POST":
        caseFilter = CaseFilter(request.POST, queryset=cases)

    context = {
        'caseFilter': caseFilter
    }
    '''
    return render(request, 'case_app/case_list.html', context)