from django.db import models

# Create your models here.


class TSDReceivingForm(models.Model):
    project_title = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    abc = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    aoname = models.CharField(max_length=100)
    fundyear = models.CharField(max_length=100)
    fund_source = models.CharField(max_length=100)
    object_of_expenditure = models.CharField(max_length=100)
    validator = models.CharField(max_length=100)
    canvasser = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.project_number