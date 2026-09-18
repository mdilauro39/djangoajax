from ..models import Agente
from django.shortcuts import get_object_or_404

# Nueva vista para el modal
def detalle_agente_modal(request, agente_id):
    agente = get_object_or_404(Agente, id=agente_id)
    return render(request, 'agentes/partials/modal_detalle.html', {'agente': agente})
