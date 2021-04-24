from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from . import models
class FinanceListView(ListView):
    print("MemberView")
    context_object_name='finance'
    model= models.Finance
    template_name='finance_app/finance_list.html'

class FinanceDetailView(DetailView):
    
    context_object_name='finance_detail'
    model=models.Finance
    template_name='finance_app/finance_detail.html'


class FinanceCreateView(CreateView):
    fields=('status','title','out_name','in_name','amount','dollor','created_from','created_at')
    model=models.Finance
    success_url= reverse_lazy("finance_app:list")
class FinanceUpdateView(UpdateView):
    fields=('status','title','out_name','in_name','amount','dollor','created_from','created_at')
    model=models.Finance
    success_url= reverse_lazy("finance_app:list")
class FinanceDeleteView(DeleteView):
    model=models.Finance
    success_url= reverse_lazy("finance_app:list")