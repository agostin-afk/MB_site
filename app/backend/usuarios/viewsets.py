from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import login

class CreateUserViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = ()

class LoginViewSet(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    queryset = MyUserBase.objects.all()
    permission_classes = ()