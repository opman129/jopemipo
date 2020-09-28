from django.urls import reverse
from django.db import models
from django.conf import settings

# Create your models here.
class PortfolioForm(models.Model):
    Name = models.CharField(blank=True, null=False, max_length=40)
    Email = models.EmailField(blank=True, null=False, max_length=40)
    Subject = models.CharField(max_length=50)
    Message = models.TextField(null=False, max_length=45)


    def __str__(self):
        return self.Name
