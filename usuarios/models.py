from django.db import models
from django.contrib.auth.models import User

from endereco.models import Cidades

# Create your models here.

class Perfil(models.Model):
    nome = models.CharField(max_length=50, null=True, verbose_name='nome')
    sobrenome = models.CharField(max_length=50, null=True,verbose_name='Sobrenome')
    telefone = models.CharField(max_length=16, null=True,verbose_name='Telefone')
    logradouro = models.CharField(max_length=100, verbose_name='Logradouro')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    numero = models.IntegerField(default=0, verbose_name='Número')
    cep = models.IntegerField(default=0, verbose_name='CEP')
    complemento = models.CharField(max_length=100, verbose_name='Complemento')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cidade_id = models.ForeignKey(Cidades,verbose_name='Cidade', on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Perfil'