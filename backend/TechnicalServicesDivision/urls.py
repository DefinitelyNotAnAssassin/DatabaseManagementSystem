from django.urls import path 
from TechnicalServicesDivision import views 

urlpatterns = [
    path('home', views.home, name = 'tsd home'), 
    path('database', views.database, name = 'tsd database'),
    path('edit_database', views.edit_database, name = 'tsd edit database'),
    path('secretariat', views.secretariat, name = 'tsd secretariat'),
    path('saveForm', views.save_form, name = 'tsd saveForm'),
    path('searchForm', views.search_form, name = 'tsd editForm'),   


]