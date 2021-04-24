from django.db import models
from django.urls import reverse
# Create your models here.
class Case(models.Model):
    name=models.CharField(max_length=256)
    phone=models.CharField(max_length=256)
    school=models.CharField(max_length=256)
    contribute_context=models.TextField(max_length=256) #related from outcome
    is_scholorship=models.BooleanField(null=False,default=False)
    scholorship_amount=models.IntegerField(null=True)
    total_money=models.IntegerField(null=True)
    situation=models.TextField(max_length=512,default="無")
    visited_form=models.CharField(max_length=256,null=True)
    visited_photos=models.CharField(max_length=256,null=True)
    start_date=models.DateTimeField(null=True)
    end_date=models.DateTimeField(null=True)
    created_at=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("case_app:detail", kwargs={"pk": self.pk})