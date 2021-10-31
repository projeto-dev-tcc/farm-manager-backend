from django.shortcuts import render, redirect
from .models import *
from .forms import *

def registrar_variedade(request):
    form = VariedadeForm()
    if request.method == "POST":
        form = VariedadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_variedades')
    context = {
        'form': form,
        'action': "Registrar"
    }
    return render(request, "manager/variedade/registrar_variedade.html", context)

def editar_variedade(request, id_variedade):
    variedade = Variedade.objects.get(id=id_variedade)
    form = VariedadeForm(instance=variedade)
    if request.method == "POST":
        form = VariedadeForm(request.POST, instance=variedade)
        if form.is_valid():
            form.save()
            return redirect('visualizar_variedade', id_variedade=id_variedade)

    context = {
        "form": form,
        "action": "Editar",
        "variedade": variedade
    }
    return render(request, "manager/variedade/registrar_variedade.html", context)

def listar_variedades(request):
    variedades = Variedade.objects.all()
    context = {
        'variedades': variedades,
    }
    return render(request, "manager/variedade/listar_variedades.html", context)

def visualizar_variedade(request, id_variedade):
    variedade = Variedade.objects.get(id=id_variedade)
    form = VariedadeForm(instance=variedade)
    context = {
        'variedade': variedade,
        'form': form
    }
    return render(request, "manager/variedade/visualizar_variedade.html", context)
