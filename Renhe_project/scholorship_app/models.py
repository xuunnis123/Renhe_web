from django.db import models
from django.urls import reverse
from student_app.models import Student
from school_app.models import School 
import datetime
# Create your models here.

class Scholorship(models.Model):
    is_case=models.BooleanField(verbose_name="個案戶",default=True)
    title=models.CharField(verbose_name="申請名義",max_length=256,default="第一學期獎學金")
    name=models.ForeignKey(Student,related_name='scho_student',on_delete=models.CASCADE,default="",verbose_name="姓名")
    school=models.ForeignKey(School,related_name='scho_school',on_delete=models.CASCADE,default="",verbose_name="學校")
    datetime=models.DateField(verbose_name="申請時間",blank=False,default=datetime.datetime.today().strftime("%Y-%m-%d"))
    scholorship_amount=models.IntegerField(verbose_name="獎學金金額",blank=False,null=True,default=0)
   

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("scholorship:detail", kwargs={"pk": self.pk})