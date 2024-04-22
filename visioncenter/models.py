from statistics import mode
from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=25,null=True)
    email=models.EmailField(max_length=60,null=True)
    password=models.CharField(max_length=12,null=True)

    def __str__(self) :
        return self.name