from django.urls import path
from InfrastructureCommittee import views

urlpatterns = [
    path('home', views.home, name='infrastructure home'),
    path('database', views.database, name='infrastructure database'),
    path('infra_receiving', views.infra_receiving, name='infrastructure receiving'),
    path('bidding_documents', views.bidding_documents, name='infrastructure bidding documents'),
    path('infra_masterlist', views.infra_masterlist, name='infrastructure masterlist'),
    path('update_infra', views.update_infra, name='update infrastructure'),
    path('consultancy_receiving', views.consultancy_receiving, name='infrastructure consultancy receiving'),
    path('getProjectNumbers', views.getProjectNumbers, name='get project numbers'),
    path('addInfraReceiving', views.addInfraReceiving, name='add infra receiving'),
    path('updateInfraMasterlist', views.updateInfraMasterlist, name='update infra masterlist'),
    path('searchInfraMasterlist', views.searchInfraMasterlist, name='search infra masterlist'),
]
