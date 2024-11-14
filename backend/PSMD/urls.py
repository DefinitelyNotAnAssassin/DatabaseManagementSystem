from django.urls import path 
from PSMD import views 

urlpatterns = [ 
    path('home', views.home, name = 'psmd home'),
    path('database', views.database, name = 'psmd database'),        
    path('inventory', views.inventory, name = 'psmd inventory'),    
    path('evaluation_sheet', views.evaluation_sheet, name = 'psmd evaluation sheet'),  
]