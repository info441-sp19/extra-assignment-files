from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField('name', max_length=20, unique=False)
    description = models.CharField('description', max_length=50)
    breed = models.CharField('breed', max_length=50)

