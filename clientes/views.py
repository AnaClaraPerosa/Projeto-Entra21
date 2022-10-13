from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import Clientes

# Create your views here.

class ClienteCreate(CreateView, LoginRequiredMixin, GroupRequiredMixin):
    login_url = reverse_lazy('login')
    # group_required = u"Usuários"
    template_name = 'cliente-form.html'
    fields = ['cliente_nome', 'cliente_telefone', 
            'cliente_cpf', 'cliente_email', 
            'cliente_logradouro', 'cliente_bairro',
            'cliente_numero', 'cliente_cep', 
            'cliente_complemento', 
            'cliente_obs', 'cliente_cidade_id']
    model = Clientes
    success_url = reverse_lazy('cliente-list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Clientes"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

################# UPDATE #################

class ClienteUpdate(UpdateView, LoginRequiredMixin, GroupRequiredMixin):
    login_url = reverse_lazy('login')
    group_required = u"Clientes"
    model = Clientes
    fields = ['cliente_nome', 'cliente_telefone', 
            'cliente_cpf', 'cliente_email', 
            'cliente_logradouro', 'cliente_bairro',
            'cliente_numero', 'cliente_cep', 
            'cliente_complemento', 
            'cliente_obs', 'cliente_cidade_id']
    template_name = 'cliente-update.html'
    success_url = reverse_lazy('cliente-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar cadastro de Clientes"
        context['botao'] = "Salvar"

        return context

################# DELETE #################

class ClienteDelete(DeleteView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    model = Clientes
    template_name = 'cliente-delete.html'
    success_url = reverse_lazy('cliente-list')

################# LISTA #################

class ClienteList(ListView, LoginRequiredMixin, GroupRequiredMixin):
    login_url = reverse_lazy('login')
    group_required = u"Clientes"
    model = Clientes
    template_name = 'cliente-list.html'

