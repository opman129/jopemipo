from django.urls import reverse
from django.db import models
from django.conf import settings

# Create your models here.
class PortfolioForm(models.Model):
    Name = models.CharField(blank=True, null=False, max_length=40)
    Email = models.EmailField()
    Subject = models.CharField(max_length=50)
    Message = models.TextField()


    def __str__(self):
        return self.title
