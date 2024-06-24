from django.shortcuts import render, redirect
from TechnicalServicesDivision.models import TSDReceivingForm

# Create your views here.

def home (request):
    return render(request, 'TechnicalServicesDivision/home.html')

def database (request):
    if request.method == "GET":
        return render(request, 'TechnicalServicesDivision/database.html')
    else:
        data = request.POST
        newReceiving = TSDReceivingForm(project_number = data['project_number'], project_title = data['project_title'], office = data['office'], abc = data['abc'], category = data['category'], aoname = data['aoname'], fundyear = data['fundyear'], fund_source = data['fund_source'], object_of_expenditure = data['object_of_expenditure'], validator = data['validator'], canvasser = data['canvasser'])
        newReceiving.save()
        return redirect('tsd home')
    
    
def edit_database (request):
    if request.method == "GET":
        return render(request, 'TechnicalServicesDivision/edit_database.html')
    else:
        data = request.POST
        project_number = data['project_number']
        project_title = data['project_title']
        office = data['office']
        abc = data['abc']
        category = data['category']
        aoname = data['aoname']
        fundyear = data['fundyear']
        fund_source = data['fund_source']
        object_of_expenditure = data['object_of_expenditure']
        validator = data['validator']
        canvasser = data['canvasser']
        TSDReceivingForm.objects.filter(project_number = project_number).update(project_title = project_title, office = office, abc = abc, category = category, aoname = aoname, fundyear = fundyear, fund_source = fund_source, object_of_expenditure = object_of_expenditure, validator = validator, canvasser = canvasser)
        return redirect('tsd home')
    
    
def secretariat (request):
    return render(request, 'TechnicalServicesDivision/secretariat.html')