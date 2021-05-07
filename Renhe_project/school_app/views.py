from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from . import models
from .filters import SchoolFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
class SchoolListView(ListView):
    print("School")
    #context_object_name='school'
    model= models.School
    template_name='school_app/school_list.html'
    filterset_class = SchoolFilter
    #paginate_by = 3
    def get_queryset(self):
        print("++++++")
        qs = self.model.objects.all()
        school_filtered_list = SchoolFilter(self.request.GET, queryset=qs)
        print(school_filtered_list)
        return school_filtered_list.qs
    
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
    print("shcool")
    schools = models.School.objects.all()

    schoolFilter = SchoolFilter(queryset=schools)
        
    if request.method == "POST":
        schoolFilter = SchoolFilter(request.POST, queryset=schools)
        
    context = {
        'schoolFilter': schoolFilter
    }
    return render(request, 'school_app/school_list.html', context)

def school2_filter(request):
    base_qs = models.School.objects.all().select_related('name')
    f = SchoolFilter(request.GET, queryset=base_qs)
    paginator = Paginator(f.qs, 5)
    page = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False
    context = {'page_obj': page_obj, 'paginator': paginator, 'is_paginated': is_paginated, 'filter': f, }

    return render(request, 'school_app/school_list.html', context)