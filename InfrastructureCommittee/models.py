from django.db import models

# Create your models here.

class InfrastructureCommittee(models.Model):
    account_code = models.CharField(max_length=255, blank=True, null=True)
    project_number = models.CharField(max_length=255, blank=True, null=True)
    project_title = models.CharField(max_length=255, blank=True, null=True)
    project_type = models.CharField(max_length=255, blank=True, null=True)
    abc = models.CharField(max_length=255, blank=True, null=True)
    early_procurement = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    calendar_days = models.CharField(max_length=255, blank=True, null=True)
    batch = models.CharField(max_length=255, blank=True, null=True)
    mode_of_procurement = models.CharField(max_length=255, blank=True, null=True)
    pre_bid_date = models.CharField(max_length=255, blank=True, null=True)  
    fund_source = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    mode = models.CharField(max_length=255, blank=True, null=True) 
    bid_amount = models.CharField(max_length=255, blank=True, null=True)
    pre_proc_date = models.CharField(max_length=255, blank=True, null=True)
    itb_date = models.CharField(max_length=255, blank=True, null=True)
    key_personnel = models.CharField(max_length=255, blank=True, null=True)
    major_equipment = models.CharField(max_length=255, blank=True, null=True)
    bidding_date = models.CharField(max_length=255, blank=True, null=True)
    bid_eval_date = models.CharField(max_length=255, blank=True, null=True)
    post_qua = models.CharField(max_length=255, blank=True, null=True)
    reso_date = models.CharField(max_length=255, blank=True, null=True)
    noa_date = models.CharField(max_length=255, blank=True, null=True)
    contract_date = models.CharField(max_length=255, blank=True, null=True)
    np_start = models.CharField(max_length=255, blank=True, null=True)
    np_end = models.CharField(max_length=255, blank=True, null=True)