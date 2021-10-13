from rest_framework import serializers
from manager.models import Fazenda

# Serializers define the API representation.        
class FazendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fazenda
        fields = ('__all__')