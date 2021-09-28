from rest_framework import viewsets
from .models import *
from django.contrib.auth.models import User
from .serializers import *

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FazendaViewSet(viewsets.ModelViewSet):
    queryset = Fazenda.objects.all()
    serializer_class = FazendaSerializer
    
class MaquinarioViewSet(viewsets.ModelViewSet):
    queryset = Maquinario.objects.all()
    serializer_class = MaquinarioSerializer
    
class VariedadeViewSet(viewsets.ModelViewSet):
    queryset = Variedade.objects.all()
    serializer_class = VariedadeSerializer
    
class TalhaoViewSet(viewsets.ModelViewSet):
    queryset = Talhao.objects.all()
    serializer_class = TalhaoSerializer
    
class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
