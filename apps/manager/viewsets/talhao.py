from rest_framework import viewsets
from manager.serializers import TalhaoSerializer
from manager.models import Talhao

# ViewSets define the view behavior.    
class TalhaoViewSet(viewsets.ModelViewSet):
    queryset = Talhao.objects.all()
    serializer_class = TalhaoSerializer
    