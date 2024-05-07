from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.



class Account(AbstractUser): 
    employee_id = models.IntegerField(null = True, blank = True)
    department = models.CharField(max_length=100, null = True, blank = True)
    position = models.CharField(max_length=100, null = True, blank = True)
    phone_number = models.CharField(max_length=100, null = True, blank = True)
    address = models.CharField(max_length=100, null = True, blank = True)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)
        super().save(*args, **kwargs)

