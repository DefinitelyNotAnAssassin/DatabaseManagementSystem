from django.forms import ModelForm 



from InfrastructureCommittee.models import InfrastructureCommittee 



class InfrastructureCommitteeForm(ModelForm): 
    class Meta: 
        model = InfrastructureCommittee 
        fields = '__all__'