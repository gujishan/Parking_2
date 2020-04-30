from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    mobile=models.CharField(max_length=11,default='')