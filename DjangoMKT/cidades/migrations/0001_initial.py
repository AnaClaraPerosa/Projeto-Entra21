# Generated by Django 4.1.1 on 2022-09-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade_nome', models.CharField(max_length=100, verbose_name='Cidade')),
                ('cidade_cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('cidade_ativo', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
                'ordering': ['cidade_nome', 'cidade_cep'],
            },
        ),
    ]
