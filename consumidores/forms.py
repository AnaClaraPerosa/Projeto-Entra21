from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Consumidores

class ConsumidoresForm(forms.ModelForm):

    class Meta:
        model = Consumidores
        field_list = ['apelido', 'cpf']
        
        # field_list = ['apelido', 'cpf', 
        #     'consumidor_logradouro', 'consumidor_bairro',
        #     'consumidor_numero', 'consumidor_cep', 
        #     'consumidor_complemento', 
        #     'consumidor_obs', 'consumidor_cidade_id'
        #     ]
            