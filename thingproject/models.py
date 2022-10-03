from django.contrib.auth.models import AbstractUser
from django.db import models

class Thing(AbstractUser):

     name= models.CharField(blank=False, unique= True, max_length=30)
     description = models.CharField(unique= False,blank=True,max_length=120)
     quantity = models.IntegerField(unique=False, min_length=0,max_length=100,)
