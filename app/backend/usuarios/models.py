from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
import re
class Perfil(models.Model):
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"
        
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo= models.CharField(max_length=255, blank=True, default='')
    email = models.EmailField(max_length=245)
    def __str__(self) -> str:
        return f'{self.usuario}'
    
    def clean(self) -> None:
        error_messages = {}
        
        email_enviado = self.email or None
        email_salvo = None
        
        perfil= Perfil.objects.filter(email=email_enviado).first()
        if perfil:
            email_salvo = perfil.email
            
            if email_salvo is not None and self.pk != perfil.pk:
                error_messages['email'] = "email já existe"
        # if re.search(r'[^0-9]', self.nome_completo) or len(self.nome_completo) < 8:
            # error_messages['nome_completo'] = 'Nome inválido'
        if error_messages:
            raise ValueError(error_messages)
