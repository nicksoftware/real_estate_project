from django.db import models
from datetime import datetime
# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    position = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hired_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name