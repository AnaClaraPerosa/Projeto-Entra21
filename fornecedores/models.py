from django.contrib.auth.models import User
from django.db import models
from endereco.models import Cidades

# Create your models here.

class Fornecedores(models.Model):
    fornecedor_nome = models.CharField(max_length=255,verbose_name='Nome')
    fornecedor_cnpj = models.CharField(max_length=20, verbose_name='CNPJ')
    fornecedor_email = models.EmailField(max_length=100, verbose_name='Email')
    fornecedor_telefone = models.CharField(max_length=30, verbose_name='Telefone')
    fornecedor_logradouro = models.CharField(max_length=100, verbose_name='Logradouro')
    fornecedor_bairro = models.CharField(max_length=100, verbose_name='Bairro')
    fornecedor_numero = models.IntegerField(default=0, verbose_name='Número')
    fornecedor_cep = models.IntegerField(default=0, verbose_name='CEP')
    fornecedor_complemento = models.CharField(max_length=100, verbose_name='Complemento')
    fornecedor_obs = models.CharField(max_length=100, verbose_name='Obs')
    fornecedor_cidade = models.ForeignKey(Cidades,verbose_name='Cidade', on_delete=models.PROTECT)
    fornecedor_ativo = models.CharField(max_length=1)
    fornecedor_criem = models.DateTimeField(auto_now_add=True)
    fornecedor_cripor = models.OneToOneField(User,related_name='fornecedor',on_delete=models.CASCADE)

    class Meta:
        ordering = ['fornecedor_nome']
        verbose_name = 'fornecedor'
        verbose_name_plural = 'fornecedores'

    def __str__(self):
        return self.fornecedor_nome
