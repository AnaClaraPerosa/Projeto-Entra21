from django.db import models

# Create your models here.

from produtos.models import Produto
from fornecedores.models import Fornecedores

class Pedido(models.Model):
    primeiro_nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    quant_paga =models.DecimalField(max_digits=8, decimal_places=2)
    fornecedores = models.ManyToManyField(Fornecedores, related_name='pedidos')
    
    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.primeiro_nome

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='itens', on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedores, related_name='itens', on_delete=models.CASCADE)
    fornecedor_pago = models.BooleanField(default=False)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id

