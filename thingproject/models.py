from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

class Thing(AbstractUser):

     name= models.CharField(blank=False, unique= True, max_length=30)
     description = models.CharField(unique= False,blank=True,max_length=120)
     quantity = models.IntegerField(
           validators=[MaxValueValidator(
               limitValue=100
           ),
                       MinValueValidator(
                       limitValue=0
                       )

           ]


     )
