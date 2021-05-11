from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from . import models
from .filters import StudentFilter
class StudentListView(ListView):
    print("StudentView")
    context_object_name='student'
    model= models.Student
    template_name='student_app/student_list.html'

class StudentDetailView(DetailView):
    
    context_object_name='student_detail'
    model=models.Student
    template_name='student_app/student_detail.html'


class StudentCreateView(CreateView):
    fields=('case_id','name','phone','school','address','is_scholorship','is_end','start_date','end_date','memo','visit_form','visit_photo')
    model=models.Student
    success_url= reverse_lazy("student_app:list")
  
class StudentUpdateView(UpdateView):
    print("Update")
    fields=('case_id','name','phone','school','address','is_scholorship','is_end','start_date','end_date','memo','visit_form','visit_photo')
    model=models.Student
    success_url= reverse_lazy("student_app:list")
class StudentDeleteView(DeleteView):
    model=models.Student
    success_url= reverse_lazy("student_app:list")

def student_filter(request):
    print("student")
    students = models.Student.objects.all()

    studentFilter = StudentFilter(queryset=students)
        
    if request.method == "POST":
        studentFilter = StudentFilter(request.POST, queryset=students)
        
    context = {
        'studentFilter': studentFilter
    }
    return render(request, 'school_app/student_list.html', context)