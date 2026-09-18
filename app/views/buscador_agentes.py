from django.shortcuts import render
from django.core.paginator import Paginator
from ..models import Agente

def buscador_agentes(request):
    # 1. Consulta base con los agentes ordenados por nombre
    agentes_queryset = Agente.objects.all().order_by('nombre')
    
    # 2. Capturar parámetros de los filtros desde la URL (Request GET)
    query = request.GET.get('q', '').strip()
    especialidad = request.GET.get('especialidad', '').strip()
    ciudad = request.GET.get('ciudad', '').strip()
    activo_ahora = request.GET.get('activo_ahora', '').strip()
    fin_semana = request.GET.get('fin_semana', '').strip()

    # 3. Aplicación dinámica de filtros del formulario
    if query:
        agentes_queryset = agentes_queryset.filter(nombre__icontains=query)
    if especialidad:
        agentes_queryset = agentes_queryset.filter(especialidad=especialidad)
    if ciudad:
        agentes_queryset = agentes_queryset.filter(ciudad=ciudad)
    if activo_ahora == 'true':
        agentes_queryset = agentes_queryset.filter(activo_ahora=True)
    if fin_semana == 'true':
        agentes_queryset = agentes_queryset.filter(disponible_fin_semana=True)

    # 4. Paginación: Mostrar 4 agentes por página (ideal para probar el paginador con pocos datos)
    paginator = Paginator(agentes_queryset, 4)
    page_number = request.GET.get('page', 1)
    agentes_paginados = paginator.get_page(page_number)

    # 5. Listados únicos para popular dinámicamente los campos select del formulario
    context = {
        'agentes': agentes_paginados,
        'especialidades': dict(Agente.ESPECIALIDADES).keys(),
        'ciudades': Agente.objects.values_list('ciudad', flat=True).distinct().order_by('ciudad'),
    }

    # ✨ INTERCEPCIÓN HTMX ✨
    # Si la petición es enviada por HTMX, renderiza EXCLUSIVAMENTE las tarjetas y el paginador
    if request.headers.get('HX-Request'):
        return render(request, 'agentes/partials/lista_resultados.html', context)

    # Primera carga del navegador: Envía la interfaz completa con la barra lateral de filtros
    return render(request, 'agentes/buscador.html', context)