from django.shortcuts import render

# Create your views here.


def database(request):
    return render(request, 'PSMD/database.html')


def inventory(request):
    return render(request, 'PSMD/inventory.html')