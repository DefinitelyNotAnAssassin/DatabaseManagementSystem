from django.forms import ModelForm, CharField, PasswordInput
from TechnicalServicesDivision.models import TSDReceivingForm 


class TechnicalServicesDivisionForm(ModelForm): 
    class Meta: 
        model = TSDReceivingForm 
        fields = ['project_title', 'office', 'abc', 'category', 'aoname', 'fundyear', 'fund_source', 'object_of_expenditure', 'validator', 'canvasser']
        
      