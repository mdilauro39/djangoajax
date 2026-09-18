from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscador_agentes, name='buscador_agentes'),
    path('agente/<int:agente_id>/modal/', views.detalle_agente_modal, name='detalle_agente_modal'), # <-- Nueva URL
]
