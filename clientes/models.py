from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from endereco.models import Cidades
from django.contrib.auth.models import User

#Create your models here.

def user_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'usuario_{0}/{1}'.format(instance.user.id, filename)

class Clientes(models.Model):
    cliente_nome = models.CharField(max_length=100,verbose_name='Nome')
    cliente_datanasc = models.DateField(null=True, blank=True, verbose_name = 'Data de Nascimento')
    cliente_telefone = models.CharField(max_length=100,verbose_name='Telefone')
    cliente_cpf = models.CharField(max_length=100,verbose_name='CPF')
    cliente_email = models.EmailField(max_length=100, verbose_name='Email')
    cliente_logradouro = models.CharField(max_length=100, verbose_name='Logradouro')
    cliente_bairro = models.CharField(max_length=100, verbose_name='Bairro')
    cliente_numero = models.IntegerField(default=0, verbose_name='Número')
    cliente_cep = models.IntegerField(default=0, verbose_name='CEP')
    cliente_complemento = models.CharField(max_length=100,blank=True, verbose_name='Complemento')
    cliente_obs = models.CharField(max_length=100, blank=True, verbose_name='Observações')
    cliente_cidade_id = models.ForeignKey(Cidades,verbose_name='Cidade', on_delete=models.PROTECT)
    cliente_ativo = models.CharField(max_length=1)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='cliente')

    def __str__(self):
        return '%s %s %s' % (self.cliente_nome, self.cliente_telefone, self.cliente_cpf)

    class Meta:
        ordering = (['cliente_nome', 'cliente_telefone'])
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
