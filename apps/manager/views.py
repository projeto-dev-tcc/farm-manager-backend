from rest_framework import viewsets
from manager.serializers import *
from manager.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
    
@api_view(['GET', 'POST'])
def ListFazenda(request):
    if request.method == 'GET':
        data = Fazenda.objects.all()
        serializer = FazendaSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FazendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def DetailFazenda(request, pk):
    try:
        fazenda = Fazenda.objects.get(pk=pk)
    except Fazenda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FazendaSerializer(fazenda)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FazendaSerializer(fazenda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fazenda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def ListMaquinario(request):
    if request.method == 'GET':
        data = Maquinario.objects.all()
        serializer = MaquinarioSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MaquinarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def DetailMaquinario(request, pk):
    try:
        maquinario = Maquinario.objects.get(pk=pk)
    except Maquinario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MaquinarioSerializer(maquinario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MaquinarioSerializer(maquinario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        maquinario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def ListServico(request):
    if request.method == 'GET':
        data = Servico.objects.all()
        serializer = ServicoSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def DetailServico(request, pk):
    try:
        servico = Servico.objects.get(pk=pk)
    except Servico.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServicoSerializer(servico)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServicoSerializer(servico, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        servico.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def ListTalhao(request):
    if request.method == 'GET':
        data = Talhao.objects.all()
        serializer = TalhaoSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TalhaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def DetailTalhao(request, pk):
    try:
        talhao = Talhao.objects.get(pk=pk)
    except Talhao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TalhaoSerializer(talhao)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TalhaoSerializer(Talhao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        talhao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def ListVariedade(request):
    if request.method == 'GET':
        data = Variedade.objects.all()
        serializer = VariedadeSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VariedadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def DetailVariedade(request, pk):
    try:
        variedade = Variedade.objects.get(pk=pk)
    except Variedade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VariedadeSerializer(variedade)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VariedadeSerializer(Variedade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        variedade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)