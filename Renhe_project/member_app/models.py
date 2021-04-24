from django.db import models
from django.urls import reverse
import datetime
# Create your models here.
class Member(models.Model):
    name=models.CharField(blank=False,max_length=256)
    id_number=models.CharField(blank=False,max_length=256) #id card
    title=models.CharField(blank=False,max_length=256,default="一般會員")
    phone=models.CharField(blank=False,max_length=256) #related from outcome
    address=models.CharField(blank=False,max_length=256,default="")
    intro_by=models.CharField(blank=True,max_length=256,default="無")
    created_at=models.DateField(blank=False,default=datetime.datetime.today().strftime("%Y-%m-%d"))
    expired_at=models.DateField(blank=False,default=datetime.datetime.today().strftime("%Y-%m-%d"))
    is_member_now=models.BooleanField(default=True)
    is_donate=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("member_app:detail", kwargs={"pk": self.pk})