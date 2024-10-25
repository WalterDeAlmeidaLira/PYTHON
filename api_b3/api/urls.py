from django.urls import path
from . import views

urlpatterns = [
    path('', views.boasVindas,name='comprimentos'),
    path('dados', views.buscaDados,name='dados'),
    
]