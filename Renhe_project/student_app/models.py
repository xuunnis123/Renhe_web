from django.db import models

from django.urls import reverse
from school_app.models import School 

# Create your models here.
class Student(models.Model):
    name=models.CharField(verbose_name="姓名",max_length=256)
    phone=models.CharField(verbose_name="電話",max_length=256)
    school=models.ForeignKey(School,related_name='school_student',on_delete=models.CASCADE,verbose_name="學校")
    case_id=models.CharField(verbose_name="案號",max_length=256,default="無")
    #school = models.ForeignKey(School,on_delete=models.CASCADE,null=True, blank=True)
    address=models.CharField(verbose_name="地址",max_length=256)
    is_end=models.BooleanField(verbose_name="已結案",null=False,default=False)
    memo=models.TextField(verbose_name="備註",max_length=256)
    created_at=models.DateTimeField(auto_now=True)
    
   

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("student:detail", kwargs={"pk": self.pk})

    