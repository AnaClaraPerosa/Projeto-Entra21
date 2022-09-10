from django.db import models
from cidades.models import Cidades

#Create your models here.

class Fornecedores(models.Model):
    fornecedor_razao_social = models.CharField(max_length=100, verbose_name='Razão social')
    fornecedor_cpf_cnpj = models.CharField(max_length=20, verbose_name='CPFJ/CNPJ')
    fornecedor_email = models.EmailField(max_length=100, verbose_name='Email')
    fornecedor_telefone = models.CharField(max_length=30, verbose_name='Telefone')
    fornecedor_logradouro = models.CharField(max_length=100, verbose_name='Logradouro')
    fornecedor_bairro = models.CharField(max_length=100, verbose_name='Bairro')
    fornecedor_numero = models.IntegerField(default=0, verbose_name='Número')
    fornecedor_cep = models.IntegerField(default=0, verbose_name='CEP')
    fornecedor_complemento = models.CharField(max_length=100, verbose_name='Complemento')
    fornecedor_obs = models.CharField(max_length=100, verbose_name='Observações',default='')
    fornecedor_cidade_id = models.ForeignKey(Cidades,verbose_name='Cidade_ID', on_delete=models.PROTECT)
    fornecedor_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s %s' % (self.fornecedor_razao_social, self.fornecedor_cpf_cnpj)

    class Meta:
        ordering = (['fornecedor_razao_social', 'fornecedor_cpf_cnpj'])
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

