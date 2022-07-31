from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class User(AbstractUser):    
#     # blank=True: 폼(입력양식)에서 빈채로 저장되는 것을 허용, DB에는 ''로 저장
#     # CharField 및 TextField는 blank=True만 허용, null=True 허용 X # null=True: DB에 NULL로 저장
#     nickname = models.CharField(max_length=50)
    email = models.EmailField(blank=False, null=False)
    level = models.IntegerField(null=True,default=0)
    point = models.IntegerField(null=True,default=0)
    first_name = None
    last_name = None

    objects = CustomUserManager()
    REQUIRED_FIELDS = [ 'email']