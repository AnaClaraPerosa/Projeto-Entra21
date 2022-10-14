from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils.text import slugify
from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import Fornecedores

from produtos.models import Produto
from .forms import ProdutoForm

################ CADASTRO DE FORNCEDORES ################

class FornecedorCreate(CreateView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    # group_required = u"Usuários"
    template_name = 'fornecedor-form.html'
    fields = ['fornecedor_nome', 'fornecedor_datanasc', 'fornecedor_cnpj', 
            'fornecedor_email', 'fornecedor_telefone',
            'fornecedor_datanasc', 'fornecedor_logradouro',
            'fornecedor_bairro',
            'fornecedor_numero', 'fornecedor_cep', 
            'fornecedor_complemento', 
            'fornecedor_obs', 'fornecedor_cidade']
    model = Fornecedores
    success_url = reverse_lazy('fornecedor-list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Fornecedores"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

################# UPDATE #################

class FornecedorUpdate(UpdateView, LoginRequiredMixin, GroupRequiredMixin):
    login_url = reverse_lazy('login')
    group_required = u"Fornecedores"
    model = Fornecedores
    fields = ['fornecedor_nome', 'fornecedor_datanasc', 'fornecedor_cnpj', 
            'fornecedor_email', 'fornecedor_telefone',
            'fornecedor_datanasc', 'fornecedor_logradouro',
            'fornecedor_bairro',
            'fornecedor_numero', 'fornecedor_cep', 
            'fornecedor_complemento', 
            'fornecedor_obs', 'fornecedor_cidade']
    template_name = 'fornecedor-update.html'
    success_url = reverse_lazy('fornecedor-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar cadastro de Fornecedores"
        context['botao'] = "Salvar"

        return context

################# DELETE #################

class FornecedorDelete(DeleteView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    model = Fornecedores
    template_name = 'fornecedor-delete.html'
    success_url = reverse_lazy('fornecedor-list')

################# LISTA #################

class FornecedorList(ListView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    model = Fornecedores
    template_name = 'fornecedor-list.html'

################ PARTE QUE JÁ ESTAVA ################

def seja_fornecedor(request):
    return render(request, 'seja_fornecedor.html')


@login_required
def fornecedor_admin(request):
    fornecedor = request.user.fornecedor
    produtos = fornecedor.produtos.all()
    
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '6')

    if not (parametro_limit.isdigit() and (int(parametro_limit) > 0)):
        parametro_limit = '6'

    # novos_produtos = Produto.objects.all()

    produtos_paginator = Paginator(produtos, parametro_limit)

    try:
        page = produtos_paginator.page(parametro_page)
    except (EmptyPage, PageNotAnInteger):
        page = produtos_paginator.page(1)

    return render(request, 'fornecedor_admin.html', {'fornecedor': fornecedor, 'produtos' : page})


@login_required
def add_produto(request):

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)

        if form.is_valid():
            produto = form.save(commit=False)
            produto.fornecedor = request.user.fornecedor
            produto.slug = slugify(produto.titulo)
            produto.save()
            return redirect('fornecedor_admin')
    else:
        form = ProdutoForm()

    return render(request,'add_produto.html', {'form' : form})

@login_required
def produto_edit(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(instance=produto)

    if (request.method == 'POST'):
        form = ProdutoForm(request.POST, instance=produto)

        if form.is_valid():
            produto.save()
            return redirect('fornecedor_admin')
        else:
            return render(request, 'produto_edit.html', {'form': form, 'produto': produto})
    else:
        return render(request, 'produto_edit.html', {'form': form, 'produto': produto})



@login_required
def produto_delete(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()
    messages.info(request,'Produto apagado')
    return redirect('fornecedor_admin')
    