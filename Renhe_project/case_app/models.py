from django.db import models
from django.urls import reverse
import datetime,time
# Create your models here.
class Case(models.Model):
    name=models.CharField(verbose_name="姓名",blank=False,max_length=256)
    phone=models.CharField(verbose_name="電話",blank=False,max_length=256)
    school=models.CharField(verbose_name="學校",blank=False,max_length=256)
    contribute_context=models.TextField(verbose_name="資助項目",blank=False,max_length=256) #related from outcome
    is_scholorship=models.BooleanField(verbose_name="獎學金",default=False)
    scholorship_amount=models.IntegerField(verbose_name="獎學金金額",blank=True,default=0,null=True)
    total_money=models.IntegerField(verbose_name="目前總資助金額",blank=False,null=True,default=0)
    situation=models.TextField(verbose_name="個案情況",max_length=512,default="無")
    visited_form=models.CharField(verbose_name="訪視表",max_length=256,blank=True,default="")
    visited_photos=models.CharField(verbose_name="訪視照片",max_length=256,blank=True,default="")
    start_date=models.DateField(verbose_name="個案開始日期",blank=False,default=datetime.datetime.today().strftime("%Y-%m-%d"))
    end_date=models.DateField(verbose_name="個案結束日期",blank=True,default=datetime.datetime.today().strftime("%Y-%m-%d"))
    created_at=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("case_app:detail", kwargs={"pk": self.pk})