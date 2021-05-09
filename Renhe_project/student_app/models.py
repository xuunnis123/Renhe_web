from django.db import models

from django.urls import reverse
from school_app.models import School 
import datetime
# Create your models here.
class Student(models.Model):
    name=models.CharField(verbose_name="姓名",max_length=256)
    phone=models.CharField(verbose_name="電話",max_length=256)
    school=models.ForeignKey(School,related_name='school_student',on_delete=models.CASCADE,verbose_name="學校")
    case_id=models.CharField(verbose_name="案號",max_length=256,default="無")
    #school = models.ForeignKey(School,on_delete=models.CASCADE,null=True, blank=True)
    address=models.CharField(verbose_name="地址",max_length=256)
    is_scholorship=models.BooleanField(verbose_name="獎學金",null=False,default=False)
    content=models.CharField(verbose_name="資助內容",max_length=256,default="無")
    is_end=models.BooleanField(verbose_name="已結案",null=False,default=False)
    start_date=models.DateField(verbose_name="個案開始日期",blank=False,default=datetime.datetime.today().strftime("%Y-%m-%d"))
    end_date=models.DateField(verbose_name="個案結束日期",blank=True,default=datetime.datetime.today().strftime("%Y-%m-%d"))
    memo=models.TextField(verbose_name="備註",max_length=256)
    visit_form=models.CharField(verbose_name="訪視表",max_length=256,default="無")
    visit_photo=models.CharField(verbose_name="訪視照片",max_length=256,default="無")
    created_at=models.DateTimeField(auto_now=True)
    
   

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("student:detail", kwargs={"pk": self.pk})

    