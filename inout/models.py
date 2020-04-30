from django.db import models

# Create your models here.
from Car_w.models import Car_w


class Car(models.Model):
    Car_no=models.CharField(primary_key=True,max_length=32,unique=True)

class Parking(models.Model):
    P_Car_w_no = models.ForeignKey(Car_w, on_delete=models.CASCADE)
    P_Car_no = models.ForeignKey(Car, on_delete=models.CASCADE)
    In_time = models.DateTimeField(auto_now_add=True)
    Out_time = models.DateTimeField(null=True, blank=True)
    All_time = models.CharField(max_length=16, null=True, blank=True)
    Cat_status = models.BooleanField(default=True)
    P_Money = models.FloatField(max_length=8, null=True, blank=True)
    P_price = models.FloatField(max_length=8, null=True, blank=True, default=None)

