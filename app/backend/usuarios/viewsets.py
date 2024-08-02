from rest_framework import viewsets
from .serializers import *
from .models import *

class CreateUserViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = ()
    
class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    queryset = Perfil.objects.all()