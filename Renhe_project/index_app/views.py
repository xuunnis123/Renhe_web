
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from django.views.generic.edit import FormView

class IndexView(TemplateView):
    template_name='index.html'
    
    def get_context_data(self):
        context = super(IndexView,self).get_context_data()
        context["phone"] = '測試中文'
        return context