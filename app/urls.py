from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscador_agentes, name='buscador_agentes'),
]
