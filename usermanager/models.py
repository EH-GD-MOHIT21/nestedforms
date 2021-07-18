from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Temporarystorage(models.Model):
    email = models.EmailField(unique=True)
    otp = models.IntegerField()
    send_at = models.DateTimeField()

    @property
    def timestampnow(self):
        self.send_at = timezone.now()

class PermanentUserData(models.Model):
    index = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return str(self.index.email)