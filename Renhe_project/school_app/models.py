from django.db import models

from django.urls import reverse
# Create your models here.
class School(models.Model):
    
    name=models.CharField(verbose_name="校名",max_length=256)
    represent_person_name=models.CharField(verbose_name="負責人",max_length=256)
    represent_person_phone=models.CharField(verbose_name="負責人電話",max_length=256)
    memo=models.TextField(verbose_name="備註",max_length=512)
    
   

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("school_app:detail", kwargs={"pk": self.pk})