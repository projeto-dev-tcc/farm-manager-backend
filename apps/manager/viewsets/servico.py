from rest_framework import viewsets
from manager.serializers import ServicoSerializer
from manager.models import Servico

# ViewSets define the view behavior.    
class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
