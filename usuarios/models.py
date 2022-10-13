from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    perfil_nome = models.CharField(max_length=50, null=True)
    perfil_sobrenome = models.CharField(max_length=50, null=True)
    telefone = models.CharField(max_length=16, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
