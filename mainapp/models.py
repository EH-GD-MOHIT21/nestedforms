from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class formpublicdata(models.Model):
    code = models.CharField(max_length=100,default=0)
    title = models.CharField(max_length=100)
    mail = models.EmailField()
    creator = models.CharField(max_length=40)
    desc = models.TextField()
    questions = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()

class responses(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=40)
    mail = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    responses = models.TextField()


