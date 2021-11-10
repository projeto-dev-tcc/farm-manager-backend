from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from manager.models import Fazenda

@login_required
def index(request):
    fazendas = Fazenda.objects.filter(proprietario__id=request.user.id)
    context = {
        'fazendas': fazendas,
    }
    
    return render(request, "manager/fazenda/listar_fazendas.html", context)
