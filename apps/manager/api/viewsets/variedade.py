from rest_framework import viewsets
from manager.api.serializers import VariedadeSerializer
from manager.models import Variedade

# ViewSets define the view behavior.
class VariedadeViewSet(viewsets.ModelViewSet):
    queryset = Variedade.objects.all()
    serializer_class = VariedadeSerializer