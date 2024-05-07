from django.forms import ModelForm
from AdministrationDepartment.models import ReceivingForm 

class ReceivingFormForm(ModelForm):
    class Meta: 
        fields = '__all__'