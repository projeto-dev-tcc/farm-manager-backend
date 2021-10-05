from rest_framework import viewsets
from manager.serializers import FazendaSerializer
from manager.models import Fazenda

# ViewSets define the view behavior.
class FazendaViewSet(viewsets.ModelViewSet):
    queryset = Fazenda.objects.all()
    serializer_class = FazendaSerializer