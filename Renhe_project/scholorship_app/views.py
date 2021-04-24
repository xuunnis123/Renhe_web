from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from . import models
class ScholorshipListView(ListView):
    print("Scholorship")
    context_object_name='scholorship'
    model= models.Scholorship
    template_name='scholorship_app/scholorship_list.html'

class ScholorshipDetailView(DetailView):
    
    context_object_name='scholorship_detail'
    model=models.Scholorship
    template_name='scholorship_app/scholorship_detail.html'


class ScholorshipCreateView(CreateView):
    fields=('is_case','title','name','school','datetime','scholorship_amount')
    model=models.Scholorship
    success_url= reverse_lazy("scholorship_app:list")
class ScholorshipUpdateView(UpdateView):
    fields=('is_case','title','name','school','datetime','scholorship_amount')
    model=models.Scholorship
    success_url= reverse_lazy("scholorship_app:list")
class ScholorshipDeleteView(DeleteView):
    model=models.Scholorship
    success_url= reverse_lazy("scholorship_app:list")

