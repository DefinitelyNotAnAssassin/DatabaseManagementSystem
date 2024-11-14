from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.



class Account(AbstractUser): 
    employee_id = models.IntegerField(null = True, blank = True)
    department = models.CharField(max_length=100, null = True, blank = True)
    position = models.CharField(max_length=100, null = True, blank = True)
    phone_number = models.CharField(max_length=100, null = True, blank = True)
    address = models.CharField(max_length=100, null = True, blank = True)
    

