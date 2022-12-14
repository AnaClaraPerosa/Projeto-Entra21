# Generated by Django 4.1.1 on 2022-10-14 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('endereco', '0002_alter_cidades_options_remove_cidades_cidade_cep'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cliente_datanasc', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('cliente_telefone', models.CharField(max_length=100, verbose_name='Telefone')),
                ('cliente_cpf', models.CharField(max_length=100, verbose_name='CPF')),
                ('cliente_email', models.EmailField(max_length=100, verbose_name='Email')),
                ('cliente_logradouro', models.CharField(max_length=100, verbose_name='Logradouro')),
                ('cliente_bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cliente_numero', models.IntegerField(default=0, verbose_name='Número')),
                ('cliente_cep', models.IntegerField(default=0, verbose_name='CEP')),
                ('cliente_complemento', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('cliente_obs', models.CharField(blank=True, max_length=100, verbose_name='Observações')),
                ('cliente_ativo', models.CharField(max_length=1)),
                ('cliente_cidade_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='endereco.cidades', verbose_name='Cidade')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='cliente')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['cliente_nome', 'cliente_telefone'],
            },
        ),
    ]
