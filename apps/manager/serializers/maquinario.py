from rest_framework import serializers
from manager.models import Maquinario

# Serializers define the API representation.     
class MaquinarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Maquinario
        fields = ('__all__')