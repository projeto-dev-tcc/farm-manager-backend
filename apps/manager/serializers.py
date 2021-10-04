from rest_framework import fields, serializers
from .models import *

# Serializers define the API representation.        
class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')

class FazendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fazenda
        fields = ('__all__')
        
class MaquinarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Maquinario
        fields = ('__all__')
        
class VariedadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variedade
        fields = ('__all__')
        
class TalhaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Talhao
        fields = ('__all__')
        
class ServicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Servico
        fields = ('__all__')
    
