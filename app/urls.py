from django.urls import path
from . import views
from .views import (
    buscador_agentes,
    detalle_agente_modal,
)


urlpatterns = [
    path('', views.buscador_agentes, name='buscador_agentes'),
    path('agente/<int:agente_id>/modal/', views.detalle_agente_modal, name='detalle_agente_modal'), # <-- Nueva URL
]
