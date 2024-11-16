from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse  
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
import json

def login(request): 
    if request.method == "GET":
        return render(request, "UserAuthentication/signin.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            
            return render(request, "UserAuthentication/signin.html", {"error": "Invalid username or password"})

def register(request): 
    return render(request, "UserAuthentication/signup.html")

def logout(request): 
    auth_logout(request)
    return redirect("login")



@csrf_exempt
def verifyAccount(request): 
    data = request.body 
    data = data.decode('utf-8') 
    print(data) 
    json_data = json.loads(data) 
    username = json_data['username'] 
    password = json_data['password']
    print(username, password)
    account = authenticate(username=username, password=password)
    
    if account:
        auth_login(request, account)
        refresh = RefreshToken.for_user(account)
        
        return JsonResponse({'status': 'success',
                                'account': {
                                    'firstname': account.first_name,
                                    'lastname': account.last_name,
                                    'employee_id': account.employee_id,
                                    'department': account.department,
                                    
                                },
                                'refresh': str(refresh),
                                'access': str(refresh.access_token)})
    else:
        return HttpResponse(status=501) 


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def verifyAuth(request): 
    return JsonResponse({'status': 'success'}, safe = False)



