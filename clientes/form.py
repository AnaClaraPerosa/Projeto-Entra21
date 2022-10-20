from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Clientes
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ['cliente_nome', 'cliente_telefone', 
            'cliente_cpf', 'cliente_email', 
            'cliente_logradouro', 'cliente_bairro',
            'cliente_numero', 'cliente_cep', 
            'cliente_complemento','cliente_datanasc',
            'cliente_obs', 'cliente_cidade_id'
            ]
    