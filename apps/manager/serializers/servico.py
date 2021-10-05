from rest_framework import serializers
from manager.models import Servico

# Serializers define the API representation.            
class ServicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Servico
        fields = ('__all__')