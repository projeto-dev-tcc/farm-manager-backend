from rest_framework import viewsets
from manager.api.serializers import MaquinarioSerializer
from manager.models import Maquinario

# ViewSets define the view behavior.
class MaquinarioViewSet(viewsets.ModelViewSet):
    queryset = Maquinario.objects.all()
    serializer_class = MaquinarioSerializer