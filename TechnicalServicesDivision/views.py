from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, 'TechnicalServicesDivision/home.html')

def database (request):
    if request.method == "GET":
        return render(request, 'TechnicalServicesDivision/database.html')
    else:
        data = request.POST
        print(data)
        return render(request, 'TechnicalServicesDivision/database.html')