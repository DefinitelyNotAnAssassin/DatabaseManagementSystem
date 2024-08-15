from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'DatabaseManagementDivision/home.html')

def validation_home(request):
    return render(request, 'DatabaseManagementDivision/dmd_validation_home.html')

def public_bidding_home(request):
    return render(request, 'DatabaseManagementDivision/dmd_public_bidding_home.html')

def validation(request):
    return render(request, 'DatabaseManagementDivision/dmd_validation.html')


def goods_and_services(request):
    return render(request, 'DatabaseManagementDivision/dmd_goods_and_services.html')


def infrastructure_and_consultancy(request):
    return render(request, 'DatabaseManagementDivision/dmd_infrastructure_and_consultancy.html')

def public_bidding(request):
    return render(request, 'DatabaseManagementDivision/dmd_public_bidding.html')

def balance_checker(request):
    return render(request, 'DatabaseManagementDivision/dmd_balance_checker.html')

def balance_checker_app_id(request):
    return render(request, 'DatabaseManagementDivision/dmd_balance_checker_app_id.html')

def amendatory_list(request):
    return render(request, 'DatabaseManagementDivision/dmd_amendatory_list.html')

def amendatory_procurement_plan(request):
    return render(request, 'DatabaseManagementDivision/dmd_amendatory_procurement_plan.html')

def ppmp_finding(request):
    return render(request, 'DatabaseManagementDivision/dmd_ppmp_finding.html')