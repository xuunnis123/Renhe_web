from django.db import models

from django.urls import reverse
from school_app.models import School 
# Create your models here.
class Student(models.Model):
    case_id=models.IntegerField(null=True)
    name=models.CharField(max_length=256)
    phone=models.CharField(max_length=256)
    school=models.CharField(max_length=256,default="")
    #school = models.ForeignKey(School,on_delete=models.CASCADE,null=True, blank=True)
    address=models.CharField(max_length=256)
    is_end=models.BooleanField(null=True)
    memo=models.CharField(max_length=256)
    created_at=models.DateTimeField(null=True)
    
   

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("student:detail", kwargs={"pk": self.pk})