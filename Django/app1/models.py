from django.db import models

# Create your models here.

class Cidades(models.Model):
    cidade_nome = models.CharField(max_length=100,verbose_name='Cidade')
    cidade_cep = models.IntegerField(default=0,verbose_name='CEP')
    cidade_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s %s' % (self.cidade_nome, self.cidade_cep)

    class Meta:
        ordering = (['cidade_nome', 'cidade_cep'])
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

class Fornecedores(models.Model):
    fornecedor_razao_social = models.CharField(max_length=100, verbose_name='Razão social')
    fornecedor_cpf_cnpj = models.IntegerField(default=0, verbose_name='CNPJ')
    fornecedor_contato = models.CharField(max_length=100, verbose_name='Email')
    fornecedor_telefone = models.IntegerField(default=0, verbose_name='Telefone')
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


class Clientes(models.Model):
    cliente_nome = models.CharField(max_length=100,verbose_name='Nome')
    cliente_telefone = models.CharField(max_length=100,verbose_name='Telefone')
    cliente_cpf = models.CharField(max_length=100,verbose_name='Cpf')
    cliente_logradouro = models.CharField(max_length=100, verbose_name='Logradouro')
    cliente_bairro = models.CharField(max_length=100, verbose_name='Bairro')
    cliente_numero = models.IntegerField(default=0, verbose_name='Número')
    cliente_cep = models.IntegerField(default=0, verbose_name='CEP')
    cliente_complemento = models.CharField(max_length=100, verbose_name='Complemento')
    cliente_obs = models.CharField(max_length=100, verbose_name='Observações')
    cliente_cidade_id = models.IntegerField(verbose_name='Cidade_ID', default=0)
    cliente_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s %s' % (self.cliente_nome, self.cliente_telefone)

    class Meta:
        ordering = (['cliente_nome', 'cliente_telefone'])
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

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
    produto_segmento_id = models.IntegerField(verbose_name='Segmento_ID',default=0)
    produto_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s %s' % (self.produto_nome, self.produto_descricao)

    class Meta:
        ordering = (['produto_nome','produto_descricao'])
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Pedidos(models.Model):
    pedido_cliente_id = models.IntegerField(verbose_name='Cliente_ID',default=0)
    pedido_fornecedor_id = models.IntegerField(verbose_name='Fornecedor_ID',default=0)
    pedido_data_pedido = models.CharField(max_length=10, verbose_name='Data do pedido')
    pedido_prazo_entrega = models.CharField(max_length=10, verbose_name='Prazo da entrega')
    pedido_obs = models.CharField(max_length=100,verbose_name='Observações')
    pedido_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s' % (self.pedido_data_pedido)

    class Meta:
        ordering = (['pedido_data_pedido'])
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    

class Itensped(models.Model):
    itensped_produto_id = models.IntegerField(verbose_name='Produto_ID',default=0)
    itensped_qtde = models.IntegerField(default= 0 , verbose_name='Quantidade')
    itensped_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s' % (self.itensped_qtde)

    class Meta:
        ordering = (['itensped_qtde'])
        verbose_name = 'Itens do pedido'
        verbose_name_plural = 'Item do pedido'


