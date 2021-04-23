from django.db import models

from django.urls import reverse
# Create your models here.
class Student(models.Model):
    case_id=models.IntegerField
    name=models.CharField(max_length=256)
    phone=models.CharField(max_length=256)
    school=models.CharField(max_length=256)
    address=models.CharField(max_length=256)
    is_end=models.BooleanField
    memo=models.CharField(max_length=256)
    created_at=models.DateTimeField
    
   

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("student:detail", kwargs={"pk": self.pk})