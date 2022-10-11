import random
from django.contrib import messages
from django.shortcuts import render,get_object_or_404, redirect
from django.db.models import Q
from .forms import AddNoCarrinhoForm
from .models import Categoria, Produto
from carrinho.carrinho import Carrinho


def pesquisa(request):
    query = request.GET.get('query','')
    produtos = Produto.objects.filter(Q(titulo__icontains = query) | Q(descricao__icontains = query))

    return render(request, 'pesquisa.html', {'produtos': produtos , 'query' : query})


def produto(request, categoria_slug, produto_slug):
    carrinho = Carrinho(request)

    produto = get_object_or_404(Produto, categoria__slug = categoria_slug, slug = produto_slug)

    if request.method == 'POST':
        form = AddNoCarrinhoForm(request.POST)

        if form.is_valid():
            quantidade = form.cleaned_data['quantidade']

            carrinho.add(produto_id=produto.id ,quantidade=quantidade, update_quantidade=False)

            messages.success(request , 'O Produto foi adicionado ao carrinho')

            return redirect('produto', categoria_slug=categoria_slug, produto_slug=produto_slug)

    else:
        form = AddNoCarrinhoForm

    produto_similar = list(produto.categoria.produtos.exclude(id=produto.id))

    if len(produto_similar) >= 4:
        produto_similar = random.sample(produto_similar, 4)

    return render(request, 'produto.html', {'form' : form , 'produto' : produto, 'produto_similar' : produto_similar})

def categoria(request, categoria_slug):
    categoria = get_object_or_404(Categoria, slug = categoria_slug)

    return render(request, 'categoria.html', {'categoria' : categoria })