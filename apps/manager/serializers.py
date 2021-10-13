from rest_framework import serializers
from manager.models import Fazenda, Maquinario, Servico, Talhao, Variedade

# Serializers define the API representation.        
class FazendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fazenda
        fields = ('__all__')
    
class MaquinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquinario
        fields = ('__all__')
    
class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ('__all__')
        
class TalhaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talhao
        fields = ('__all__')

class VariedadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variedade
        fields = ('__all__')