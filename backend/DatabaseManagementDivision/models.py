from django.db import models

# Create your models here.

class AmendatoryList(models.Model): 
    ammendatory_id = models.AutoField(primary_key=True)
    requesting_office_a = models.CharField(max_length=255)
    total_amount_a = models.DecimalField(max_digits=10, decimal_places=2)
    requesting_office_b = models.CharField(max_length=255)
    total_amount_b = models.DecimalField(max_digits=10, decimal_places=2)
    particulars_item_description = models.TextField()
    reason_for_amending = models.TextField()
    validator = models.CharField(max_length=255)
    date_advance_copy = models.DateField()
    date_signed = models.DateField()
    status = models.CharField(max_length=50)
class DMD(models.Model): 
    project_number = models.CharField(max_length=255) 
    amendatorylist = models.ForeignKey('AmendatoryList', on_delete=models.CASCADE)

