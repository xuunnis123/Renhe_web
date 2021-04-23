from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from . import models
class StudentListView(ListView):
    print("StudentView")
    context_object_name='student'
    model= models.Student
    template_name='student_app/student_list.html'