from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    userID =models.CharField(max_length=200,primary_key=True)
    password = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    level = models.IntegerField(null=True,default=0)
    point = models.IntegerField(null=True,default=0)
    access = models.BooleanField(null=True,default=False)
