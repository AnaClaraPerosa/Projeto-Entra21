# Generated by Django 4.1.1 on 2022-10-13 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cidades',
            options={'ordering': ['cidade_nome'], 'verbose_name': 'Cidade', 'verbose_name_plural': 'Cidades'},
        ),
        migrations.RemoveField(
            model_name='cidades',
            name='cidade_cep',
        ),
    ]
