from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import copy
from rest_framework.views import APIView
from . import models
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics


# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer
    
# class Criar(APIView):
#     def post(self, *args, **kwargs):

#         username = self.userform.cleaned_data.get('username')
#         password = self.userform.cleaned_data.get('password')
#         email = self.userform.cleaned_data.get('email')
#         first_name = self.userform.cleaned_data.get('first_name')
#         last_name = self.userform.cleaned_data.get('last_name')
#         if self.request.user.is_authenticated:
#             usuario = get_object_or_404(User, username=self.request.user.username) #type: ignore
#             usuario.username = username
#             if password:
#                 usuario.set_password(password)
            
#             usuario.first_name = first_name
#             usuario.last_name = last_name
#             usuario.save()

#             if not self.perfil:
#                 self.perfilform.cleaned_data['usuario'] = usuario
#                 perfil = models.Perfil(**self.perfilform.cleaned_data)
#                 perfil.save()
#             else: 
#                 perfil = self.perfilform.save(commit=False)
#                 perfil.usuario = usuario
#                 perfil.save()         
#         else:
#             usuario = self.userform.save(commit=False)
#             usuario.set_password(password)
#             usuario.save()
            
#             perfil = self.perfilform.save(commit=False)
#             perfil.usuario = usuario
#             perfil.save()
#         if password:
#             autentica = authenticate(
#                 self.request,
#                 username= usuario,
#                 password= password,
#             )
#             if autentica:
#                 login(self.request, user= usuario)
#         self.request.session['carrinho'] = self.carrinho
#         self.request.session.save()
#         return redirect('perfil:CreateUser')
#         return self.renderizar


class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')


class Login(View):
    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
    
        if not username or not password:
            messages.error(
                self.request,
                'Usuário ou senha inválida',
            )
        usuario = authenticate(
            self.request,
            username=username,
            password=password,
        )
        if not usuario:
            messages.error(
                self.request,
                'Usuário ou senha inválidos'
            )
            return redirect('perfil:CreateUser')
        login(self.request, user=usuario)
        return redirect('produto:ListarProdutos')

class Logout(View):
    def get(self, *args, **kwargs):
        carrinho =  copy.deepcopy(self.request.session.get('carrinho)'))
        
        logout(self.request)
        
        self.request.session['carrinho'] = carrinho
        self.request.session.save()
        redirect('produto:ListarProdutos')