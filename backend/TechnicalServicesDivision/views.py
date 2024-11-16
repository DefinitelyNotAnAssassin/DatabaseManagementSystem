from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.db.utils import IntegrityError
from TechnicalServicesDivision.models import TSDReceivingForm
from TechnicalServicesDivision.forms import TechnicalServicesDivisionForm    
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from ProjectNumber.models import ProjectNumbers
import json


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

@api_view(['POST'])
def save_form(request): 
    data = request.body 
    data = data.decode('utf-8')  
    json_data = json.loads(data) 
    form = TechnicalServicesDivisionForm(json_data) 
    if form.is_valid(): 
        tsd = form.save()
        try: 
            ProjectNumbers.objects.create(project_number = json_data['project_number'], project_title = tsd.project_title, tsd = tsd)
        except IntegrityError as e:
            print(e)
            TSDReceivingForm.objects.get(id = tsd.id).delete()
            return JsonResponse({'status': 'error', 'message': 'Project Number is already existing'}, safe = False)
        
        print("Form saved")
        return JsonResponse({'status': 'success', 'message': 'Form saved successfully.'}, safe = False)
    else:
        return JsonResponse({'status': 'error'}, safe = False)

@csrf_exempt
@api_view(['POST']) 
def search_form(request):
    data = request.body     
    data = data.decode('utf-8') 
    json_data = json.loads(data) 
    
    filters = {} 
    
    for key in json_data.keys(): 
        if json_data[key] != '': 
            filters[key] = json_data[key] 
            
            
    #TODO: Handle OR conditions for filtering
    if json_data['project_number'] != '': 
        project_number = json_data['project_number']
        receiving = get_object_or_404(ProjectNumbers, project_number = project_number)
        receiving = receiving.tsd
        
        data = {'project_number': project_number, 
            'project_title': receiving.project_title,
            'office': receiving.office,
            'abc': receiving.abc,
            'category': receiving.category,
            'aoname': receiving.aoname,
            'fundyear': receiving.fundyear,
            'fund_source': receiving.fund_source,
            'object_of_expenditure': receiving.object_of_expenditure,
            'validator': receiving.validator,
            'canvasser': receiving.canvasser
            
        }


        return JsonResponse({'status': 'success', 'data': data}, safe = False)
    
    else: 
        receiving = TSDReceivingForm.objects.filter(**filters)
        print(receiving)
        return JsonResponse({'status': 'success', 'receiving': receiving}, safe = False)

    
     



