from django.db import models

# Create your models here.

class Cidades(models.Model):
    cidade_nome = models.CharField(max_length=100,verbose_name='Cidade')
    Cidade_cep = models.IntegerField(default=0,verbose_name='CEP')
    Cidade_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s %s' % (self.cidade_nome, self.Cidade_cep)

    class Meta:
        ordering = (['cidade_nome', 'Cidade_cep'])
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

class Fornecedores(models.Model):
    Fornecedor_razao_social = models.CharField(max_length=100, verbose_name='Razão social')
    Fornecedor_cpf_cnpj = models.IntegerField(default=0, verbose_name='CNPJ')
    Fornecedor_contato = models.CharField(max_length=100, verbose_name='Email')
    Fornecedor_telefone = models.IntegerField(default=0, verbose_name='Telefone')
    Fornecedor_logradouro = models.CharField(max_length=100, verbose_name='Logradouro')
    Fornecedor_bairro = models.CharField(max_length=100, verbose_name='Bairro')
    Fornecedor_numero = models.IntegerField(default=0, verbose_name='Número')
    Fornecedor_cep = models.IntegerField(default=0, verbose_name='CEP')
    Fornecedor_complemento = models.CharField(max_length=100, verbose_name='Complemento')
    Fornecedor_obs = models.CharField(max_length=100, verbose_name='Observações',default='')
    Fornecedor_cidade_id = models.ForeignKey(Cidades,verbose_name='Cidade_ID', on_delete=models.PROTECT)
    Fornecedor_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s %s' % (self.Fornecedor_razao_social, self.Fornecedor_cpf_cnpj)

    class Meta:
        ordering = (['Fornecedor_razao_social', 'Fornecedor_cpf_cnpj'])
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'


class Clientes(models.Model):
    Cliente_nome = models.CharField(max_length=100,verbose_name='Nome')
    Cliente_telefone = models.CharField(max_length=100,verbose_name='Telefone')
    Cliente_cpf = models.CharField(max_length=100,verbose_name='Cpf')
    Cliente_logradouro = models.CharField(max_length=100, verbose_name='Logradouro')
    Cliente_bairro = models.CharField(max_length=100, verbose_name='Bairro')
    Cliente_numero = models.IntegerField(default=0, verbose_name='Número')
    Cliente_cep = models.IntegerField(default=0, verbose_name='CEP')
    Cliente_complemento = models.CharField(max_length=100, verbose_name='Complemento')
    Cliente_obs = models.CharField(max_length=100, verbose_name='Observações')
    Cliente_cidade_id = models.IntegerField(verbose_name='Cidade_ID', default=0)
    Cliente_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s %s' % (self.Cliente_nome, self.Cliente_telefone)

    class Meta:
        ordering = (['Cliente_nome', 'Cliente_telefone'])
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Segmentos(models.Model):
    Segmento_nome = models.CharField(max_length=100,verbose_name='Segmento')
    Segmento_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s' % (self.Segmento_nome)

    class Meta:
        ordering = (['Segmento_nome'])
        verbose_name = 'Segmento'
        verbose_name_plural = 'Segmentos'


class Produtos(models.Model):
    Produto_nome = models.CharField(max_length=100,verbose_name='Produto')
    Produto_descricao = models.CharField(max_length=100,verbose_name='Descrição')
    Produto_valor_unit = models.IntegerField(default=0,verbose_name='Valor Unitário')
    Produto_qtde = models.IntegerField(default=0,verbose_name='Quantidade')
    Produto_segmento_id = models.IntegerField(verbose_name='Segmento_ID',default=0)
    Produto_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s %s' % (self.Produto_nome, self.Produto_descricao)

    class Meta:
        ordering = (['Produto_nome','Produto_descricao'])
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Pedidos(models.Model):
    Pedido_cliente_id = models.IntegerField(verbose_name='Cliente_ID',default=0)
    Pedido_fornecedor_id = models.IntegerField(verbose_name='Fornecedor_ID',default=0)
    Pedido_data_pedido = models.CharField(max_length=10, verbose_name='Data do pedido')
    Pedido_prazo_entrega = models.CharField(max_length=10, verbose_name='Prazo da entrega')
    Pedido_obs = models.CharField(max_length=100,verbose_name='Observações')
    Pedido_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s' % (self.Pedido_data_pedido)

    class Meta:
        ordering = (['Pedido_data_pedido'])
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    

class Itensped(models.Model):
    Itensped_produto_id = models.IntegerField(verbose_name='Produto_ID',default=0)
    Itensped_qtde = models.IntegerField(default= 0 , verbose_name='Quantidade')
    Itensped_ativo = models.CharField(max_length=1)

    def __str__(self):
        return '%s' % (self.Itensped_qtde)

    class Meta:
        ordering = (['Itensped_qtde'])
        verbose_name = 'Itens do pedido'
        verbose_name_plural = 'Item do pedido'

class Teste(models.Model):
    Teste_nome = models.CharField(max_length=1)

