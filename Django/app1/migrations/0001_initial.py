# Generated by Django 4.1 on 2022-08-29 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cidade_nome', models.CharField(max_length=100, verbose_name='Cidade')),
                ('Cidade_cep', models.IntegerField(default=0, verbose_name='CEP')),
                ('Cidade_ativo', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
                'ordering': ['Cidade_nome', 'Cidade_cep'],
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cliente_nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('Cliente_telefone', models.CharField(max_length=100, verbose_name='Telefone')),
                ('Cliente_cpf', models.CharField(max_length=100, verbose_name='Cpf')),
                ('Cliente_logradouro', models.CharField(max_length=100, verbose_name='Logradouro')),
                ('Cliente_bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('Cliente_numero', models.IntegerField(default=0, verbose_name='Número')),
                ('Cliente_cep', models.IntegerField(default=0, verbose_name='CEP')),
                ('Cliente_complemento', models.CharField(max_length=100, verbose_name='Complemento')),
                ('Cliente_obs', models.CharField(max_length=100, verbose_name='Observações')),
                ('Cliente_cidade_id', models.IntegerField(default=0, verbose_name='Cidade_ID')),
                ('Cliente_ativo', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['Cliente_nome', 'Cliente_telefone'],
            },
        ),
        migrations.CreateModel(
            name='Itensped',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Itensped_produto_id', models.IntegerField(default=0, verbose_name='Produto_ID')),
                ('Itensped_qtde', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('Itensped_ativo', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': 'Itens do pedido',
                'verbose_name_plural': 'Item do pedido',
                'ordering': ['Itensped_qtde'],
            },
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pedido_cliente_id', models.IntegerField(default=0, verbose_name='Cliente_ID')),
                ('Pedido_fornecedor_id', models.IntegerField(default=0, verbose_name='Fornecedor_ID')),
                ('Pedido_data_pedido', models.CharField(max_length=10, verbose_name='Data do pedido')),
                ('Pedido_prazo_entrega', models.CharField(max_length=10, verbose_name='Prazo da entrega')),
                ('Pedido_obs', models.CharField(max_length=100, verbose_name='Observações')),
                ('Pedido_ativo', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ['Pedido_data_pedido'],
            },
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Produto_nome', models.CharField(max_length=100, verbose_name='Produto')),
                ('Produto_descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('Produto_valor_unit', models.IntegerField(default=0, verbose_name='Valor Unitário')),
                ('Produto_qtde', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('Produto_segmento_id', models.IntegerField(default=0, verbose_name='Segmento_ID')),
                ('Produto_ativo', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['Produto_nome', 'Produto_descricao'],
            },
        ),
        migrations.CreateModel(
            name='Segmentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Segmento_nome', models.CharField(max_length=100, verbose_name='Segmento')),
                ('Segmento_ativo', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': 'Segmento',
                'verbose_name_plural': 'Segmentos',
                'ordering': ['Segmento_nome'],
            },
        ),
        migrations.CreateModel(
            name='Fornecedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fornecedor_razao_social', models.CharField(max_length=100, verbose_name='Razão social')),
                ('Fornecedor_cpf_cnpj', models.IntegerField(default=0, verbose_name='CNPJ')),
                ('Fornecedor_contato', models.CharField(max_length=100, verbose_name='Email')),
                ('Fornecedor_telefone', models.IntegerField(default=0, verbose_name='Telefone')),
                ('Fornecedor_logradouro', models.CharField(max_length=100, verbose_name='Logradouro')),
                ('Fornecedor_bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('Fornecedor_numero', models.IntegerField(default=0, verbose_name='Número')),
                ('Fornecedor_cep', models.IntegerField(default=0, verbose_name='CEP')),
                ('Fornecedor_complemento', models.CharField(max_length=100, verbose_name='Complemento')),
                ('Fornecedor_obs', models.CharField(default='', max_length=100, verbose_name='Observações')),
                ('Fornecedor_ativo', models.CharField(max_length=1)),
                ('Fornecedor_cidade_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.cidades', verbose_name='Cidade_ID')),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
                'ordering': ['Fornecedor_razao_social', 'Fornecedor_cpf_cnpj'],
            },
        ),
    ]