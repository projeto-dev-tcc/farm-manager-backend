from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from manager.models import Fazenda
import datetime

def base(request):
    context = {}
    if request.user.is_authenticated:
        url_path = request.path
        list_path = []
        if len(url_path) == 1:
            list_path.append('/')
        else:
            for url in url_path[1:]:
                if url == '/':
                    break
                else:
                    list_path.append(url)
                
        url_active = "".join(list_path)
        
        print(f"\n{url_path}\n")
        
        date = datetime.datetime.now().date()
        context = {
            'year': date.year,
            'url_active': url_active
        }
    return context

@login_required
def index(request):
    fazendas = Fazenda.objects.filter(proprietario__id=request.user.id)
    context = {
        'fazendas': fazendas,
    }
    
    return render(request, "manager/fazenda/listar_fazendas.html", context)
