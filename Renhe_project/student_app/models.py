from django.db import models

from django.urls import reverse
from school_app.models import School 
from case_app.models import Case
# Create your models here.
class Student(models.Model):
    case_id=models.ForeignKey(Case,related_name='case_student',on_delete=models.CASCADE,default="")
    name=models.CharField(max_length=256)
    phone=models.CharField(max_length=256)
    school=models.ForeignKey(School,related_name='school_student',on_delete=models.CASCADE)
    #school = models.ForeignKey(School,on_delete=models.CASCADE,null=True, blank=True)
    address=models.CharField(max_length=256)
    is_end=models.BooleanField(null=False,default=False)
    memo=models.TextField(max_length=256)
    created_at=models.DateTimeField(auto_now=True)
    
   

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("student:detail", kwargs={"pk": self.pk})

    