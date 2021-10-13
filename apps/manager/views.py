from rest_framework import viewsets
from manager.serializers import FazendaSerializer
from manager.models import Fazenda
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