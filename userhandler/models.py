from django.db import models

# Create your models here.

class registration_form(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    phoneno = models.CharField(max_length=20)
    age = models.IntegerField()

