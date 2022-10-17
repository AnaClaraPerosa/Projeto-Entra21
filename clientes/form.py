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
            
    # def form_valid(self, form):

    #     grupo = get_object_or_404(Group, name="Clientes")

    #     url = super().form_valid(form)

    #     self.object.groups.add(grupo)
    #     self.object.save()

    #     Clientes.objects.create(usuario=self.object)

    #     return url

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)

    #     context['titulo'] = "Cadastro de Clientes"
    #     context['botao'] = "Cadastrar"
    #     context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

    #     return context