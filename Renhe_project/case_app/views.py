from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from . import models
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

class CaseUpdateView(UpdateView):
    fields=('phone','school','contribute_context','is_scholorship','scholorship_amount','total_money','situation','visited_form','visited_photos','start_date','end_date')
    model=models.Case

class CaseDeleteView(DeleteView):
    model=models.Case
    success_url= reverse_lazy("case_app:list")