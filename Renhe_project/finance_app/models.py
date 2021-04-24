from django.db import models
from django.urls import reverse
import datetime
from student_app.models import Student
from member_app.models import Member
# Create your models here.

class Finance(models.Model):
    FINANCE_OUTCOME = 'o'
    FINANCE_INCOME = 'i'
    FINANCE_CHOICES = [
    (FINANCE_OUTCOME, '支出'),
    (FINANCE_INCOME, '收入'),
    ]
    status=models.CharField(max_length=256,choices=FINANCE_CHOICES,default=FINANCE_OUTCOME)
    title=models.CharField(blank=False,max_length=256,default="日常支出")
    out_name=models.ForeignKey(Student,related_name='fin_student',on_delete=models.CASCADE,default="")
    in_name=models.ForeignKey(Member,related_name='fin_member',on_delete=models.CASCADE,default="")
    amount=models.IntegerField(default=0)
    dollor=models.CharField(default="NTD",max_length=256)
    created_from=models.CharField(max_length=256)
    created_at=models.DateField(blank=True,default=datetime.datetime.today().strftime("%Y-%m-%d"))
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("finance:detail", kwargs={"pk": self.pk})