from django.db import models
from django.urls import reverse
import datetime
# Create your models here.
class Member(models.Model):
    name=models.CharField(verbose_name="姓名",blank=False,max_length=256)
    id_number=models.CharField(verbose_name="身分證",blank=False,max_length=256) #id card
    title=models.CharField(verbose_name="職位",blank=False,max_length=256,default="一般會員")
    phone=models.CharField(verbose_name="電話",blank=False,max_length=256) #related from outcome
    address=models.CharField(verbose_name="地址",blank=False,max_length=256,default="")
    intro_by=models.CharField(verbose_name="介紹人",blank=True,max_length=256,default="無")
    created_at=models.DateField(verbose_name="加入日期",blank=False,default=datetime.datetime.today().strftime("%Y-%m-%d"))
    expired_at=models.DateField(verbose_name="會員失效日期",blank=False,default=datetime.datetime.today().strftime("%Y-%m-%d"))
    is_member_now=models.BooleanField(verbose_name="會員身份",default=True)
    is_donate=models.BooleanField(verbose_name="會費繳納",default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("member_app:detail", kwargs={"pk": self.pk})