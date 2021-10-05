from rest_framework import serializers
from manager.models import Talhao

# Serializers define the API representation.      
class TalhaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Talhao
        fields = ('__all__')