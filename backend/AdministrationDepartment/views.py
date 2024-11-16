
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from AdministrationDepartment.models import ReceivingForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
import json


def home(request):
    return render(request, 'AdministrationDepartment/home.html')


def database(request):
    if request.method == "GET": 
        return render(request, 'AdministrationDepartment/database.html')
    else:
        data = request.POST 
        print(data)
        newForm = ReceivingForm(pd_routing_number = "PD-" + data['pd_routing_number'] + "-" + data['pd_id'], year = data['year'], received_by = data['received_by'], sender = data['sender'], office_code = data['office_code'], end_user = data['end_user'], document_type = data['document_type'], program = data['program']) 
        newForm.save()
        return redirect('administration home')
    
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def receiving(request):
    data = request.body 
    data = data.decode('utf-8')
    json_data = json.loads(data)
    try:
        ReceivingForm.objects.create(pd_routing_number = json_data['pd_routing_number'], year = json_data['year'], received_by = json_data['received_by'], sender = json_data['sender'], office_code = json_data['office_code'], end_user = json_data['end_user'], document_type = json_data['document_type'], program = json_data['program'])
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'error'}, safe = False)
    return JsonResponse({'status': 'success'}, safe = False)