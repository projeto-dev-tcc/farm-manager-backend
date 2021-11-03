from django.shortcuts import render, redirect
from .validate import validate_variedade
from .models import *
from .forms import *
from usuarios.validate import group_required
from django.contrib import messages

GPAdmin = "Administrador"
GPCliente = "Cliente"

# FAZENDAS
def registrar_fazenda(request):
    form = FazendaForm()
    if request.method == "POST":
        form = FazendaForm(request.POST)
        if form.is_valid():
            fazenda = form.save(commit=False)
            fazenda.proprietario = request.user
            fazenda.save()
            message = f"A fazenda {fazenda.nome} foi registrada com sucesso!"
            messages.success(request, message)
            return redirect('listar_fazendas')
    context = {
        'form': form,
        'action': "Registrar"
    }
    return render(request, "manager/fazenda/registrar_fazenda.html", context)

def editar_fazenda(request, id_fazenda):
    fazenda = Fazenda.objects.get(id=id_fazenda)
    form = FazendaForm(instance=fazenda)
    if request.method == "POST":
        form = FazendaForm(request.POST, instance=fazenda)
        if form.is_valid():
            form.save()
            return redirect('visualizar_fazenda', id_fazenda=id_fazenda)

    context = {
        "form": form,
        "action": "Editar",
        "fazenda": fazenda
    }
    
    return render(request, "manager/fazenda/registrar_fazenda.html", context)

def listar_fazendas(request):
    fazendas = Fazenda.objects.filter(proprietario__id=request.user.id)
    context = {
        'fazendas': fazendas,
    }
    
    return render(request, "manager/fazenda/listar_fazendas.html", context)

def painel_administrativo(request, id_fazenda):
    fazenda = Fazenda.objects.get(id=id_fazenda)
    context = {
        'fazenda': fazenda,
    }
    return render(request, "manager/fazenda/painel_administrativo.html", context)

def visualizar_fazenda(request, id_fazenda):
    fazenda = Fazenda.objects.get(id=id_fazenda)
    context = {
        'fazenda': fazenda,
    }
    return render(request, "manager/fazenda/visualizar_fazenda.html", context)

def remover_fazenda(request, id_fazenda):
    fazenda = Fazenda.objects.get(id=id_fazenda)
    fazenda.delete()
    
    return redirect("listar_fazendas")

# VARIEDADES
def registrar_variedade(request):
    form = VariedadeForm()
    if request.method == "POST":
        form = VariedadeForm(request.POST)
        nome = request.POST.get('nome', None)
        if validate_variedade(nome):
            if form.is_valid():
                variedade = form.save(commit=False)
                variedade.nome = nome
                variedade.save()
                
                message = f"A fazenda {variedade.nome} foi registrada com sucesso!"
                messages.success(request, message)
                
                return redirect('listar_variedades')
    context = {
        'form': form,
        'action': "Registrar"
    }
    return render(request, "manager/variedade/registrar_variedade.html", context)

@group_required(GPAdmin)
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

@group_required(GPAdmin)
def remover_variedade(request, id_variedade):
    variedade = Variedade.objects.get(id=id_variedade)
    variedade.delete()
    
    return redirect("listar_variedades")

# MAQUINÁRIOS
def registrar_maquinario(request):
    form = MaquinarioForm()
    if request.method == "POST":
        form = MaquinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_maquinarios')
    context = {
        'form': form,
        'action': "Registrar"
    }
    return render(request, "manager/maquinario/registrar_maquinario.html", context)

def editar_maquinario(request, id_maquinario):
    maquinario = Maquinario.objects.get(id=id_maquinario)
    form = MaquinarioForm(instance=maquinario)
    if request.method == "POST":
        form = MaquinarioForm(request.POST, instance=maquinario)
        if form.is_valid():
            form.save()
            return redirect('visualizar_maquinario', id_maquinario=id_maquinario)

    context = {
        "form": form,
        "action": "Editar",
        "maquinario": maquinario
    }
    
    return render(request, "manager/maquinario/registrar_maquinario.html", context)

def listar_maquinarios(request, id_fazenda):
    maquinarios = Maquinario.objects.filter(fazenda__id=id_fazenda)
    context = {
        'maquinarios': maquinarios,
    }
    
    return render(request, "manager/maquinario/listar_maquinarios.html", context)

def visualizar_maquinario(request, id_maquinario):
    maquinario = Maquinario.objects.get(id=id_maquinario)
    form = MaquinarioForm(instance=maquinario)
    context = {
        'maquinario': maquinario,
        'form': form
    }
    
    return render(request, "manager/maquinario/visualizar_maquinario.html", context)

def remover_maquinario(request, id_maquinario):
    maquinario = Maquinario.objects.get(id=id_maquinario)
    maquinario.delete()
    
    return redirect("listar_maquinarios")

# TALHÕES
def registrar_talhao(request):
    form = TalhaoForm()
    if request.method == "POST":
        form = TalhaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_talhoes')
    context = {
        'form': form,
        'action': "Registrar"
    }
    return render(request, "manager/talhao/registrar_talhao.html", context)

def editar_talhao(request, id_talhao):
    talhao = Talhao.objects.get(id=id_talhao)
    form = TalhaoForm(instance=talhao)
    if request.method == "POST":
        form = TalhaoForm(request.POST, instance=talhao)
        if form.is_valid():
            form.save()
            return redirect('visualizar_talhao', id_talhao=id_talhao)

    context = {
        "form": form,
        "action": "Editar",
        "talhao": talhao
    }
    
    return render(request, "manager/talhao/registrar_talhao.html", context)

def listar_talhoes(request, id_fazenda):
    talhoes = Talhao.objects.filter(fazenda__id=id_fazenda)
    context = {
        'talhoes': talhoes,
    }
    
    return render(request, "manager/talhao/listar_talhoes.html", context)

def visualizar_talhao(request, id_talhao):
    talhao = Talhao.objects.get(id=id_talhao)
    context = {
        'talhao': talhao,
    }
    return render(request, "manager/talhao/visualizar_talhao.html", context)

def remover_talhao(request, id_talhao):
    talhao = Talhao.objects.get(id=id_talhao)
    talhao.delete()
    
    return redirect("listar_talhoes")
