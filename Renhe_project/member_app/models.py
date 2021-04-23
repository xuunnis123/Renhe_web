from django.db import models
from django.urls import reverse
# Create your models here.
class Member(models.Model):
    name=models.CharField(max_length=256)
    id_number=models.CharField(max_length=256) #id card
    title=models.CharField(max_length=256)
    phone=models.CharField(max_length=256) #related from outcome
    address=models.CharField
    intro_by=models.CharField
    created_at=models.DateTimeField
    expired_at=models.DateTimeField
    is_member_now=models.BooleanField
    is_donate=models.BooleanField

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("member_app:detail", kwargs={"pk": self.pk})