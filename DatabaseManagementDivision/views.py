from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'DatabaseManagementDivision/home.html')

def validation(request):
    return render(request, 'DatabaseManagementDivision/dmd_validation.html')


def goods_and_services(request):
    return render(request, 'DatabaseManagementDivision/dmd_goods_and_services.html')


def infrastructure_and_consultancy(request):
    return render(request, 'DatabaseManagementDivision/dmd_infrastructure_and_consultancy.html')

def public_bidding(request):
    return render(request, 'DatabaseManagementDivision/dmd_public_bidding.html')