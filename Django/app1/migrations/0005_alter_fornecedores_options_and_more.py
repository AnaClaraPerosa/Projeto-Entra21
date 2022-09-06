# Generated by Django 4.1 on 2022-08-30 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_cidades_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fornecedores',
            options={'ordering': ['fornecedor_razao_social', 'fornecedor_cpf_cnpj'], 'verbose_name': 'Fornecedor', 'verbose_name_plural': 'Fornecedores'},
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='Fornecedor_ativo',
            new_name='fornecedor_ativo',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='Fornecedor_bairro',
            new_name='fornecedor_bairro',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='Fornecedor_cep',
            new_name='fornecedor_cep',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='Fornecedor_cidade_id',
            new_name='fornecedor_cidade_id',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='Fornecedor_complemento',
            new_name='fornecedor_complemento',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='Fornecedor_contato',
            new_name='fornecedor_contato',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='Fornecedor_cpf_cnpj',
            new_name='fornecedor_cpf_cnpj',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='Fornecedor_logradouro',
            new_name='fornecedor_logradouro',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='Fornecedor_numero',
            new_name='fornecedor_numero',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='Fornecedor_obs',
            new_name='fornecedor_obs',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='Fornecedor_razao_social',
            new_name='fornecedor_razao_social',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='Fornecedor_telefone',
            new_name='fornecedor_telefone',
        ),
    ]