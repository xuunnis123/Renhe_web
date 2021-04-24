from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from . import models
class FileListView(ListView):
    print("File")
    context_object_name='file'
    model= models.File
    template_name='file_app/file_list.html'

class FileDetailView(DetailView):
    
    context_object_name='file_detail'
    model=models.File
    template_name='file_app/file_detail.html'


class FileCreateView(CreateView):
    fields=('name','data')
    model=models.File
    success_url= reverse_lazy("file_app:list")
class FileUpdateView(UpdateView):
    fields=('name','data')
    model=models.File
    success_url= reverse_lazy("file_app:list")
class FileDeleteView(DeleteView):
    model=models.File
    success_url= reverse_lazy("file_app:list")