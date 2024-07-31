from rest_framework import viewsets
from .serializers import *
from .models import *


class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    queryset = Perfil.objects.all()