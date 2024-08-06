from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import re

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_superuser(self, email, date_of_birth, password=None):
    #     user = self.create_user(
    #         email,
    #         password=password,
    #         date_of_birth=date_of_birth,
    #     )
    #     user.is_admin = True
    #     user.save(using=self._db)
    #     return user

# class Perfil(models.Model):
#     class Meta:
#         verbose_name = "Perfil"
#         verbose_name_plural = "Perfis"
        
#     usuario = models.OneToOneField(User, on_delete=models.CASCADE)
#     nome_completo= models.CharField(max_length=255, blank=True, default='')
#     email = models.EmailField(max_length=245)
#     def __str__(self) -> str:
#         return f'{self.usuario}'
    
#     def clean(self) -> None:
#         error_messages = {}
        
#         email_enviado = self.email or None
#         email_salvo = None
        
#         perfil= Perfil.objects.filter(email=email_enviado).first()
#         if perfil:
#             email_salvo = perfil.email
            
#             if email_salvo is not None and self.pk != perfil.pk:
#                 error_messages['email'] = "email já existe"
#         # if re.search(r'[^0-9]', self.nome_completo) or len(self.nome_completo) < 8:
#             # error_messages['nome_completo'] = 'Nome inválido'
#         if error_messages:
#             raise ValueError(error_messages)
class MyUserBase(AbstractBaseUser):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True,)
    password = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    REQUIRED_FIELDS = ["password", "email", "username", "first_name", "last_name"]
    
    objects = MyUserManager()
    def __str__(self):
        return self.username

