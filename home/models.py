from itertools import product
from unicodedata import category, name
from django.db import models

# Create your models here.
class Contact(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.CharField(max_length=12)
    message = models.TextField()

    def __str__(self):

        return self.name
    