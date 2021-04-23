from django.db import models
from django.urls import reverse
# Create your models here.
class Case(models.Model):
    name=models.CharField(max_length=256)
    phone=models.CharField(max_length=256)
    school=models.CharField(max_length=256)
    contribute_context=models.CharField(max_length=256) #related from outcome
    is_scholorship=models.BooleanField
    scholorship_amount=models.IntegerField
    total_money=models.IntegerField
    situation=models.CharField
    visited_form=models.CharField
    visited_photos=models.CharField
    start_date=models.DateTimeField
    end_date=models.DateTimeField
    created_at=models.DateTimeField
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("case_app:detail", kwargs={"pk": self.pk})