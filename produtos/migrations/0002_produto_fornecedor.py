# Generated by Django 4.1.1 on 2022-10-14 13:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0001_initial'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='fornecedores.fornecedores'),
            preserve_default=False,
        ),
    ]
