from django.urls import path 
from DatabaseManagementDivision import views


urlpatterns = [ 
    path('home', views.home, name='dmd home'),      
    path('validation', views.validation, name='dmd validation'), 
    path('goods_and_services', views.goods_and_services, name='dmd goods and services'), 
    path('infrastructure_and_consultancy', views.infrastructure_and_consultancy, name='dmd infrastructure and consultancy'),
    path('public_bidding', views.public_bidding, name='dmd public bidding'),      
]