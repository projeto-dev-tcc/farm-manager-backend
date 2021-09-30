from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Fazenda
from .serializers import *

@api_view(['GET', 'POST'])
def list_fazenda(request):
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

@api_view(['PUT', 'DELETE'])
def detail_fazenda(request, pk):
    try:
        fazenda = Fazenda.objects.get(pk=pk)
    except Fazenda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = FazendaSerializer(fazenda, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fazenda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)