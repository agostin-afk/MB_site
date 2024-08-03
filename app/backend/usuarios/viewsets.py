from rest_framework import viewsets
from .serializers import *
from .models import *

class CreateUserViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = ()
    
class LoginViewSet(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    queryset = User.objects.all()
    permission_classes = ()
    