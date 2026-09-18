# views/__init__.py
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.paginator import Paginator
from ..models import Agente
from django.shortcuts import get_object_or_404

from .buscador_agentes import (
    buscador_agentes
)

from .detalle_agente_modal import (
    detalle_agente_modal
)