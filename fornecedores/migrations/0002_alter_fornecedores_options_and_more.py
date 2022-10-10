# Generated by Django 4.1.1 on 2022-10-10 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('fornecedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fornecedores',
            options={'ordering': ['fornecedor_razao'], 'verbose_name': 'fornecedor', 'verbose_name_plural': 'fornecedores'},
        ),
        migrations.RemoveField(
            model_name='fornecedores',
            name='fornecedor_bairro',
        ),
        migrations.RemoveField(
            model_name='fornecedores',
            name='fornecedor_cep',
        ),
        migrations.RemoveField(
            model_name='fornecedores',
            name='fornecedor_complemento',
        ),
        migrations.RemoveField(
            model_name='fornecedores',
            name='fornecedor_cpf_cnpj',
        ),
        migrations.RemoveField(
            model_name='fornecedores',
            name='fornecedor_email',
        ),
        migrations.RemoveField(
            model_name='fornecedores',
            name='fornecedor_logradouro',
        ),
        migrations.RemoveField(
            model_name='fornecedores',
            name='fornecedor_nome',
        ),
        migrations.RemoveField(
            model_name='fornecedores',
            name='fornecedor_numero',
        ),
        migrations.RemoveField(
            model_name='fornecedores',
            name='fornecedor_telefone',
        ),
        migrations.AddField(
            model_name='fornecedores',
            name='fornecedor_razao',
            field=models.CharField(default='none', max_length=255, verbose_name='Razão'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fornecedores',
            name='fornecedor_cripor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fornecedor', to='usuarios.perfil'),
        ),
    ]
