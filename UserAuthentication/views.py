from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.


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