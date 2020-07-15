from django.db import models
from datetime import datetime
# Create your models here.
class Police(models.Model):
    username = models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=32,blank=False) 

    def __str__(self):
        return self.username

class Location(models.Model):
    android_id = models.CharField(max_length=256,unique=True,blank=False)
    latitude = models.CharField(max_length=32,blank=False)
    longitude = models.CharField(max_length=32,blank=False)
    address = models.CharField(max_length=256)
    state = models.CharField(default= "Delhi",max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    def __str__(self):
        return self.android_id