# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255, verbose_name='Full Name', default='Default Name')
    email = models.EmailField(unique=True, verbose_name='Email')
    username = models.CharField(max_length=50, unique=True, verbose_name='Username')
    password = models.CharField(max_length=255, verbose_name='Password')
    agree_to_terms = models.BooleanField(default=False, verbose_name='Agree to Terms of Use')

    def __str__(self):
        return self.username
