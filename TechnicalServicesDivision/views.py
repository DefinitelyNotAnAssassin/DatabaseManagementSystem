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