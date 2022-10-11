from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import Consumidores

# Create your views here.

class ConsumidorCreate(CreateView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    # group_required = [u"Administrador", u"Clientes"]
    template_name = 'consumidor-form.html'
    fields = ['consumidor_nome', 'consumidor_telefone', 
            'consumidor_cpf', 'consumidor_email', 
            'consumidor_logradouro', 'consumidor_bairro',
            'consumidor_numero', 'consumidor_cep', 
            'consumidor_complemento', 
            'consumidor_obs', 'consumidor_cidade_id']
    model = Consumidores
    success_url = reverse_lazy('consumidor-list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Consumidores"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

################# UPDATE #################

class ConsumidorUpdate(UpdateView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    model = Consumidores
    fields = ['consumidor_nome', 'consumidor_telefone', 
            'consumidor_cpf', 'consumidor_email', 
            'consumidor_logradouro', 'consumidor_bairro',
            'consumidor_numero', 'consumidor_cep', 
            'consumidor_complemento', 
            'consumidor_obs', 'consumidor_cidade_id']
    template_name = 'consumidor-update.html'
    success_url = reverse_lazy('consumidor-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar cadastro de Consumidores"
        context['botao'] = "Salvar"

        return context

################# DELETE #################

class ConsumidorDelete(DeleteView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    model = Consumidores
    template_name = 'consumidor-delete.html'
    success_url = reverse_lazy('consumidor-list')

################# LISTA #################

class ConsumidorList(ListView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    model = Consumidores
    template_name = 'consumidor-list.html'

####################