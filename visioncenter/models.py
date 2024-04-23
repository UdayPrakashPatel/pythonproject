from statistics import mode
from django.db import models
# Create your models here.
# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    direction = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        # Specify unique related names for reverse relationships
        # This resolves the clashes identified by the system check
        # Replace 'customuser_' with any unique related name you prefer
        permissions = [
            ("customuser_can_do_something", "Can do something"),
        ]

    # Add related_name attribute to resolve clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_permissions'
    )



class Employee(models.Model):
    name=models.CharField(max_length=25,null=True)
    email=models.EmailField(max_length=60,null=True)
    password=models.CharField(max_length=12,null=True)

    def __str__(self) :
        return self.name