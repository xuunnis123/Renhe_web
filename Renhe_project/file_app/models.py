from django.db import models
from django.urls import reverse
# Create your models here.
class File(models.Model):
    name=models.CharField(verbose_name="檔名",max_length=256)
    data=models.URLField(verbose_name="下載路徑",max_length=256)
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("file_app:detail", kwargs={"pk": self.pk})