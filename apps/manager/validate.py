from .models import Adubo, Fazenda, Maquinario, Talhao, Variedade
from django.core import serializers
from django.http import HttpResponse

def validate_variedade(nome):
    try:
        variedade = Variedade.objects.get(nome__contains = nome)
        if variedade:
            return False
        return True
    except Variedade.DoesNotExist:
        return True

def Ajax_cadastrar_trator(request):
    idFazenda = request.GET.get('idFazenda', None)
    objFazenda = Fazenda.objects.get(pk = idFazenda)
    marca = request.GET.get('marca', None)
    modelo = request.GET.get('modelo', None)
    anoFabricacao = request.GET.get('anoFabricacao', None)
    observacoes = request.GET.get('observacoes', None)
    
    try:
        objMaquinario = Maquinario()
        objMaquinario.fazenda = objFazenda
        objMaquinario.marca = marca
        objMaquinario.modelo = modelo
        objMaquinario.ano_fabricacao = anoFabricacao
        objMaquinario.observacoes = observacoes
        objMaquinario.tipo = 1
        objMaquinario.save()
    except:
        pass
        

    listMaquinarios = Maquinario.objects.filter(fazenda = objFazenda, tipo = 1)
    data = serializers.serialize('json', listMaquinarios)
    return HttpResponse(data, content_type="application/json")


def Ajax_cadastrar_implemento(request):
    idFazenda = request.GET.get('idFazenda', None)
    objFazenda = Fazenda.objects.get(pk = idFazenda)
    marca = request.GET.get('marca', None)
    modelo = request.GET.get('modelo', None)
    anoFabricacao = request.GET.get('anoFabricacao', None)
    observacoes = request.GET.get('observacoes', None)

    try:
        objMaquinario = Maquinario()
        objMaquinario.fazenda = objFazenda
        objMaquinario.marca = marca
        objMaquinario.modelo = modelo
        objMaquinario.ano_fabricacao = anoFabricacao
        objMaquinario.observacoes = observacoes
        objMaquinario.tipo = 2
        objMaquinario.save()
    except:
        pass
        

    listMaquinarios = Maquinario.objects.filter(fazenda = objFazenda, tipo = 2)
    data = serializers.serialize('json', listMaquinarios)
    return HttpResponse(data, content_type="application/json")


def Ajax_cadastrar_talhao(request):
    idFazenda = request.GET.get('idFazenda', None)
    objFazenda = Fazenda.objects.get(pk = idFazenda)
    nome = request.GET.get('nome', None)
    anoPlantio = request.GET.get('anoPlantio', None)
    numueroCovas = request.GET.get('numueroCovas', None)
    espacamentoRua = request.GET.get('espacamentoRua', None)
    espacamentoCova = request.GET.get('espacamentoCova', None)
    area = request.GET.get('area', None)
    numeroCovasHectare = request.GET.get('numeroCovasHectare', None)
    listIdsVariedade = request.GET.getlist('idVariedade[]', None)
    listVariedade = Variedade.objects.filter(pk__in=listIdsVariedade)

    try:
        objTalhao = Talhao()
        objTalhao.fazenda = objFazenda
        objTalhao.nome = nome
        objTalhao.ano_plantio = anoPlantio
        objTalhao.numero_covas = numueroCovas
        objTalhao.espacamento_rua = espacamentoRua
        objTalhao.espacamento_cova = espacamentoCova
        objTalhao.area = area
        objTalhao.numero_covas_hectare = numeroCovasHectare
        objTalhao.save()
        objTalhao.variedade.add(listVariedade) 
        
    except:
        pass

    listTalhoes = Talhao.objects.filter(fazenda = objFazenda)

    data = serializers.serialize('json', listTalhoes)
    return HttpResponse(data, content_type="application/json")

def Ajax_cadastrar_adubo(request):
    nome = request.GET.get('nome', None)
    try:
        objAdubo = Adubo()
        objAdubo.nome = nome
        objAdubo.save()
        
    except:
        pass

    listAdubo = Adubo.objects.all()

    data = serializers.serialize('json', listAdubo)
    return HttpResponse(data, content_type="application/json")
