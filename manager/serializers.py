from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

# Serializers define the API representation.        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
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
    
