from django.db import models
from django.urls import reverse
import datetime,time
# Create your models here.
class Case(models.Model):
    name=models.CharField(blank=False,max_length=256)
    phone=models.CharField(blank=False,max_length=256)
    school=models.CharField(blank=False,max_length=256)
    contribute_context=models.TextField(blank=False,max_length=256) #related from outcome
    is_scholorship=models.BooleanField(default=False)
    scholorship_amount=models.IntegerField(blank=True,default=0,null=True)
    total_money=models.IntegerField(blank=False,null=True,default=0)
    situation=models.TextField(max_length=512,default="無")
    visited_form=models.CharField(max_length=256,blank=True,default="")
    visited_photos=models.CharField(max_length=256,blank=True,default="")
    start_date=models.DateField(blank=False,default=datetime.datetime.today().strftime("%Y-%m-%d"))
    end_date=models.DateField(blank=True,default=datetime.datetime.today().strftime("%Y-%m-%d"))
    created_at=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("case_app:detail", kwargs={"pk": self.pk})