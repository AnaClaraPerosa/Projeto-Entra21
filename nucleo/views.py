from multiprocessing import context
from queue import Empty
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from produtos.models import Produto
from produtos.views import produto


def index(request):
    produto = Produto.objects.order_by('?').all()
    context = {
        'produto1' : produto
    }
    return render(request,'index.html', context)

def pagamento(request):
    return render(request,'pagamento.html')



def contato(request):
    return render(request,'contato.html')

def depoimentos(request):
    return render(request,'depoimentos.html')


def loja(request):
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '8')


    if not (parametro_limit.isdigit() and (int(parametro_limit) > 0)):
        parametro_limit = '8'

    # novos_produtos = Produto.objects.all()[0:8]
    novos_produtos = Produto.objects.all()

    produtos_paginator = Paginator(novos_produtos, parametro_limit)
    
    try:
        page = produtos_paginator.page(parametro_page)
    except (EmptyPage, PageNotAnInteger):
        page = produtos_paginator.page(1)


    context = {
        'novos_produtos' : page
    }
    return render(request,'loja.html', context)
