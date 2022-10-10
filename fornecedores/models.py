from django.db import models

from usuarios.models import Perfil

# Create your models here.

class Fornecedores(models.Model):
    fornecedor_razao = models.CharField(max_length=255,verbose_name='Razão')
    fornecedor_ativo = models.CharField(max_length=1)
    fornecedor_criem = models.DateTimeField(auto_now_add=True)
    fornecedor_cripor = models.ForeignKey(Perfil,related_name='fornecedor',on_delete=models.CASCADE)

    class Meta:
        ordering = ['fornecedor_razao']
        verbose_name = 'fornecedor'
        verbose_name_plural = 'fornecedores'

    def __str__(self):
        return self.fornecedor_razao
