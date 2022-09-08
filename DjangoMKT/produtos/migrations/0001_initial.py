# Generated by Django 4.1.1 on 2022-09-08 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Segmentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segmento_nome', models.CharField(max_length=100, verbose_name='Segmento')),
                ('segmento_ativo', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': 'Segmento',
                'verbose_name_plural': 'Segmentos',
                'ordering': ['segmento_nome'],
            },
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto_nome', models.CharField(max_length=100, verbose_name='Produto')),
                ('produto_descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('produto_valor_unit', models.IntegerField(default=0, verbose_name='Valor Unitário')),
                ('produto_qtde', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('produto_ativo', models.CharField(max_length=1)),
                ('produto_segmento_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produtos.segmentos', verbose_name='Segmento_ID')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['produto_nome', 'produto_descricao'],
            },
        ),
    ]
