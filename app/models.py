from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Dashboard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    
    def __str__(self):
        return self.title


class List(models.Model):
    title = models.CharField(max_length=200)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)


    def __str__(self):
        return self.title