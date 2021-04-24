from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from . import models
class MemberListView(ListView):
    print("MemberView")
    context_object_name='member'
    model= models.Member
    template_name='member_app/member_list.html'

class MemberDetailView(DetailView):
    
    context_object_name='member_detail'
    model=models.Member
    template_name='member_app/member_detail.html'


class MemberCreateView(CreateView):
    fields=('name','id_number','title','phone','address','intro_by','created_at','expired_at','is_member_now','is_donate')
    model=models.Member
    success_url= reverse_lazy("member_app:list")
class MemberUpdateView(UpdateView):
    fields=('title','phone','address','intro_by','created_at','expired_at','is_member_now','is_donate')
    model=models.Member
    success_url= reverse_lazy("member_app:list")
class MemberDeleteView(DeleteView):
    model=models.Member
    success_url= reverse_lazy("member_app:list")