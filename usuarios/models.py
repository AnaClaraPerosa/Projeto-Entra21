from django.db import models
from django.contrib.auth.models import User

from endereco.models import Cidades

# Create your models here.

class Perfil(models.Model):
    perfil_nome = models.CharField(max_length=50, null=True, verbose_name='Nome')
    perfil_sobrenome = models.CharField(max_length=50, null=True,verbose_name='Sobrenome')
    perfil_telefone = models.CharField(max_length=16, null=True,verbose_name='Telefone')
    perfil_logradouro = models.CharField(max_length=100, verbose_name='Logradouro')
    perfil_bairro = models.CharField(max_length=100, verbose_name='Bairro')
    perfil_numero = models.IntegerField(default=0, verbose_name='Número')
    perfil_cep = models.IntegerField(default=0, verbose_name='CEP')
    perfil_complemento = models.CharField(max_length=100, verbose_name='Complemento')
    perfil_cpf_cnpj = models.CharField(max_length=20, verbose_name='CPFJ/CNPJ')
    perfil_email = models.EmailField(max_length=100, verbose_name='Email')
    perfil_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    perfil_cidade_id = models.ForeignKey(Cidades,verbose_name='Cidade', on_delete=models.PROTECT)
class Meta:
        ordering = ['perfil_nome']
        verbose_name = 'perfil'