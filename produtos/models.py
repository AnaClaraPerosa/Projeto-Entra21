from django.db import models

#Create your models here.


class Segmentos(models.Model):
    segmento_nome = models.CharField(max_length=100,verbose_name='Segmento')
    segmento_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s' % (self.segmento_nome)

    class Meta:
        ordering = (['segmento_nome'])
        verbose_name = 'Segmento'
        verbose_name_plural = 'Segmentos'


class Produtos(models.Model):
    produto_nome = models.CharField(max_length=100,verbose_name='Produto')
    produto_descricao = models.CharField(max_length=100,verbose_name='Descrição')
    produto_valor_unit = models.IntegerField(default=0,verbose_name='Valor Unitário')
    produto_qtde = models.IntegerField(default=0,verbose_name='Quantidade')
    produto_segmento_id = models.ForeignKey(Segmentos,verbose_name='Segmento_ID', on_delete=models.PROTECT)
    produto_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s %s' % (self.produto_nome, self.produto_descricao)

    class Meta:
        ordering = (['produto_nome','produto_descricao'])
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
