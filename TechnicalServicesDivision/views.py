from django.shortcuts import render, redirect
from TechnicalServicesDivision.models import TSDReceivingForm
from TechnicalServicesDivision.forms import TechnicalServicesDivisionForm    
from ProjectNumber.models import ProjectNumbers


# Create your views here.

def home (request):
    return render(request, 'TechnicalServicesDivision/home.html')

def database (request):
    if request.method == "GET":
        return render(request, 'TechnicalServicesDivision/database.html')
    else:
        data = request.POST
        newReceiving = TechnicalServicesDivisionForm(data)
        newReceiving = newReceiving.save()
        print(newReceiving)
        new_pn = ProjectNumbers.objects.create(project_number = data['project_number'], project_title = newReceiving.project_title, tsd = newReceiving)

        new_pn.save()   
        
        return redirect('tsd home')
    
    
def edit_database (request):
    if request.method == "GET":
        project_number = request.GET.get('project_number', '')
        
        if project_number != '':
            receiving = ProjectNumbers.objects.get(project_number = project_number)
            receiving = receiving.tsd   
            
            if receiving is None:
                return render(request, 'TechnicalServicesDivision/edit_database.html')
            else:
                return render(request, 'TechnicalServicesDivision/edit_database.html', {'receiving': receiving})
    
        else:
            return render(request, 'TechnicalServicesDivision/edit_database.html')
        
    elif request.method == "POST":
        data = request.POST
        
        updateReceiving = TechnicalServicesDivisionForm(data, instance = TSDReceivingForm.objects.get(id = data['id']))
        updateReceiving.save()
        return redirect('tsd home')
    
    
    
def secretariat (request):
    return render(request, 'TechnicalServicesDivision/secretariat.html')