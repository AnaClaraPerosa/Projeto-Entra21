from django.db import models

from usuarios.models import Perfil

# Create your models here.

class Fornecedores(models.Model):
    razao = models.CharField(max_length=255,verbose_name='Razão')
    ativo = models.CharField(max_length=1)
    criem = models.DateTimeField(auto_now_add=True)
    cripor = models.ForeignKey(Perfil,related_name='Fornecedor',on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=20, verbose_name='CNPJ')
    class Meta:
        ordering = ['razao']
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.razao
