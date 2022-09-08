from django.db import models

#Create your models here.

class Cidades(models.Model):
    cidade_nome = models.CharField(max_length=100,verbose_name='Cidade')
    cidade_cep = models.CharField(max_length=10,verbose_name='CEP')
    cidade_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s %s' % (self.cidade_nome, self.cidade_cep)

    class Meta:
        ordering = (['cidade_nome', 'cidade_cep'])
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'