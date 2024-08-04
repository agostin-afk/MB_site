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
    queryset = User.objects.all()
    permission_classes = ()
    # def post(self, request, validated_data,*args, **kwargs):
    #     serializer = LoginSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user = validated_data.get('user')
    #         login(request, user)
    #         token, created = Token.objects.get_or_create(user=user)
    #         return Response({'token': token.key}, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)