from rest_framework import viewsets
from .models import *
from .serializers import *

# ViewSets define the view behavior.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer