from django.db import models
from django.urls import reverse
# Create your models here.
class Scholorship(models.Model):
    is_case=models.BooleanField
    name=models.CharField(max_length=256)
    datetime=models.DateTimeField
    scholorship_amount=models.IntegerField
   

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("scholorship:detail", kwargs={"pk": self.pk})