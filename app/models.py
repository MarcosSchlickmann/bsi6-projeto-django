from django.db import models

# Create your models here.

class Category(models.model):
    title = models.CharField()
    description = models.CharField()
