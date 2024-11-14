from django.urls import path 
from UserAuthentication import views

urlpatterns = [ 
        path("login", views.login, name = "login"),
        path("register", views.register, name = "register"),
        path("logout", views.logout, name = "logout"), 
        path("verifyAccount", views.verifyAccount, name = "verifyAccount"),      
        path("verifyAuth", views.verifyAuth, name = "verifyAuth"),      
               ]