from django.urls import path 
from DatabaseManagementDivision import views


urlpatterns = [ 
    path('home', views.home, name='dmd home'),    
    path('validation_home', views.validation_home, name='dmd validation home'),  
    path('public_bidding_home', views.public_bidding_home, name='dmd public bidding home'),
    path('validation', views.validation, name='dmd validation'), 
    path('goods_and_services', views.goods_and_services, name='dmd goods and services'), 
    path('infrastructure_and_consultancy', views.infrastructure_and_consultancy, name='dmd infrastructure and consultancy'),
    path('public_bidding', views.public_bidding, name='dmd public bidding'),   
    path('balance_checker', views.balance_checker, name='dmd balance checker'),   
    path('balance_checker_app_id', views.balance_checker_app_id, name='dmd balance checker app id'),
    path('amendatory_list', views.amendatory_list, name='dmd amendatory list'),
    path('amendatory_procurement_plan', views.amendatory_procurement_plan, name='dmd amendatory procurement plan'),
    path('ppmp_finding', views.ppmp_finding, name='dmd ppmp finding'),
]