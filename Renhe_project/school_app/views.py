from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from . import models
from .filters import SchoolFilter
class SchoolListView(ListView):
    print("School")
    context_object_name='school'
    model= models.School
    template_name='school_app/school_list.html'

class SchoolDetailView(DetailView):
    
    context_object_name='school_detail'
    model=models.School
    template_name='school_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields=('name','represent_person_name','represent_person_phone','memo')
    model=models.School
    success_url= reverse_lazy("school_app:list")
   
class SchoolUpdateView(UpdateView):
    print("Update")
    fields=('represent_person_name','represent_person_phone','memo')
    model=models.School
    success_url= reverse_lazy("school_app:list")
class SchoolDeleteView(DeleteView):
    model=models.School
    success_url= reverse_lazy("school_app:list")



def school_filter(request):
    school = models.School.objects.all()

    f = SchoolFilter(request.GET, queryset=models.School.objects.filter(name=''))
    context = {'filter': f, }
    print("context:",f)
    '''
    caseFilter = CaseFilter(queryset=cases)

    if request.method == "POST":
        caseFilter = CaseFilter(request.POST, queryset=cases)

    context = {
        'caseFilter': caseFilter
    }
    '''
    return render(request, 'school_app/school_list.html', context)