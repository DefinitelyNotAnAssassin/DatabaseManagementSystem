from django.db import models

class ReceivingForm(models.Model):
    pd_routing_number = models.CharField(max_length=20)
    year = models.IntegerField()
    received_by = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    office_code = models.CharField(max_length=50)
    end_user = models.CharField(max_length=100)
    document_type = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    
    date_received = models.DateField(auto_now_add=True)
    time_received = models.TimeField(auto_now_add=True)
    transmitted_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.pd_routing_number} - {self.year}"