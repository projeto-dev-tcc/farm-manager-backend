from rest_framework import fields, serializers
from .models import *

# Serializers define the API representation.        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')