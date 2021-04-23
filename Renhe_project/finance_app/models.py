from django.db import models
from django.urls import reverse
# Create your models here.
class EnumField(models.Field):
    def __init__(self, *args, **kwargs):
        super(EnumField, self).__init__(*args, **kwargs)
        if not self.choices:
            raise AttributeError('EnumField requires `choices` attribute.')
    
    
    
FINANCE_OUTCOME = 'o'
FINANCE_INCOME = 'i'
FINANCE_CHOICES = (
    (FINANCE_OUTCOME, 'Outcome'),
    (FINANCE_INCOME, 'Income'),
)
class Finance(models.Model):
    status=EnumField(choices=FINANCE_CHOICES)
    title=models.CharField(max_length=256)
    name=models.CharField(max_length=256) #id card
    amount=models.IntegerField
    dollor=models.CharField(default="NTD",max_length=256)
    created_from=models.CharField(max_length=256)
    created_at=models.DateTimeField
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("finance:detail", kwargs={"pk": self.pk})