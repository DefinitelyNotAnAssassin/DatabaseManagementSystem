from django.urls import path 
from AdministrationDepartment import views

urlpatterns = [
    path('home', views.home, name = 'administration home'), 
    path('database', views.database, name = 'administration database')
]