from django.db import models

from django.urls import reverse
# Create your models here.
class School(models.Model):
    
    name=models.CharField(max_length=256)
    represent_person_name=models.CharField(max_length=256)
    represent_person_phone=models.CharField(max_length=256)
    memo=models.CharField(max_length=256)
    
   

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("school_app:detail", kwargs={"pk": self.pk})