from rest_framework import serializers
from manager.models import Variedade

# Serializers define the API representation.      
class VariedadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variedade
        fields = ('__all__')