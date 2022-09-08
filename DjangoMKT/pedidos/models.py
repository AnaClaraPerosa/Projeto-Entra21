from django.db import models
from fornecedores.models import Fornecedores
from clientes.models import Clientes
from produtos.models import Produtos

#Create your models here.

class Pedidos(models.Model):
    pedido_cliente_id = models.ForeignKey(Clientes,verbose_name='Cliente_ID', on_delete=models.PROTECT)
    pedido_fornecedor_id = models.ForeignKey(Fornecedores,verbose_name='Fornecedor_ID', on_delete=models.PROTECT)
    pedido_data_pedido = models.DateField(verbose_name='Data do pedido')
    pedido_prazo_entrega = models.DateField(verbose_name='Prazo da entrega')
    pedido_obs = models.CharField(max_length=100,verbose_name='Observações')
    pedido_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s' % (self.pedido_data_pedido)

    class Meta:
        ordering = (['pedido_data_pedido'])
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    

class Itensped(models.Model):
    itensped_produto_id = models.ForeignKey(Produtos,verbose_name='Produto_ID', on_delete=models.PROTECT)
    itensped_qtde = models.IntegerField(default= 0 , verbose_name='Quantidade')
    itensped_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s' % (self.itensped_qtde)

    class Meta:
        ordering = (['itensped_qtde'])
        verbose_name = 'Itens do pedido'
        verbose_name_plural = 'Item do pedido'
