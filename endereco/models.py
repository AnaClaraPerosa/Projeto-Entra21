from django.db import models

# Create your models here.

class Estados(models.Model):
    estado_nome = models.CharField(max_length=50)
    estado_uf = models.CharField(max_length=2, verbose_name='UF')

    def __str__(self):
        return '%s %s' % (self.estado_nome, self.estado_uf)
    
    class Meta:
        ordering = (['estado_nome', 'estado_uf'])
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


class Cidades(models.Model):
    cidade_nome = models.CharField(max_length=100,verbose_name='Cidade')
    cidade_ativo = models.CharField(max_length=1)
    cidade_estado = models.ForeignKey(Estados, max_length=20, on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % (self.cidade_nome)

    class Meta:
        ordering = (['cidade_nome'])
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
