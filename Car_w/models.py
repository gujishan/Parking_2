from django.db import models

# Create your models here.

# 车位信息表
class Car_w(models.Model):
    Car_w_no = models.IntegerField(primary_key=True, unique=True, null=False, blank=False)
    Car_w_wz=models.CharField(max_length=16)
    Car_w_length = models.FloatField(max_length=16)
    Car_w_status = models.BooleanField(default=True)