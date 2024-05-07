
from django.shortcuts import render, redirect
from AdministrationDepartment.models import ReceivingForm
# Create your views here.


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