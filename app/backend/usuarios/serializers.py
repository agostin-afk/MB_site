from .models import *
from rest_framework import serializers


class PerfilSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Perfil
        fields = '__all__'