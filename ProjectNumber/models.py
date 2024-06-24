from django.db import models
import uuid
# Create your models here.


class ProjectNumbers(models.Model): 
    project_unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_number = models.CharField(max_length=100, unique=True) 
    project_title = models.CharField(max_length=100)    
    tsd = models.ForeignKey('TechnicalServicesDivision.TSDReceivingForm', on_delete=models.CASCADE)
    #dmd = models.ForeignKey('DMD', on_delete=models.CASCADE)
    #psmd = models.ForeignKey('PSMD', on_delete=models.CASCADE)
    