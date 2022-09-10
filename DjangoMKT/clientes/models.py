from django.db import models
from cidades.models import Cidades

#Create your models here.

class Clientes(models.Model):
    cliente_nome = models.CharField(max_length=100,verbose_name='Nome')
    cliente_telefone = models.CharField(max_length=100,verbose_name='Telefone')
    cliente_cpf = models.CharField(max_length=100,verbose_name='CPF')
    cliente_email = models.EmailField(max_length=100, verbose_name='Email')
    cliente_logradouro = models.CharField(max_length=100, verbose_name='Logradouro')
    cliente_bairro = models.CharField(max_length=100, verbose_name='Bairro')
    cliente_numero = models.IntegerField(default=0, verbose_name='Número')
    cliente_cep = models.IntegerField(default=0, verbose_name='CEP')
    cliente_complemento = models.CharField(max_length=100, verbose_name='Complemento')
    cliente_obs = models.CharField(max_length=100, verbose_name='Observações')
    cliente_cidade_id = models.ForeignKey(Cidades,verbose_name='Cidade_ID', on_delete=models.PROTECT)
    cliente_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s %s' % (self.cliente_nome, self.cliente_telefone)

    class Meta:
        ordering = (['cliente_nome', 'cliente_telefone'])
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
