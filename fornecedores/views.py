from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils.text import slugify
from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Fornecedores
from produtos.models import Produto
from .forms import ProdutoForm


def seja_fornecedor(request):
    return render(request, 'seja_fornecedor.html')


# @login_required
# def fornecedor_admin(request):
#     fornecedor = request.user.fornecedor
#     produtos = fornecedor.produtos.all()
    
#     parametro_page = request.GET.get('page', '1')
#     parametro_limit = request.GET.get('limit', '6')

#     if not (parametro_limit.isdigit() and (int(parametro_limit) > 0)):
#         parametro_limit = '6'

#     # novos_produtos = Produto.objects.all()

#     produtos_paginator = Paginator(produtos, parametro_limit)

#     try:
#         page = produtos_paginator.page(parametro_page)
#     except (EmptyPage, PageNotAnInteger):
#         page = produtos_paginator.page(1)

#     return render(request, 'fornecedor_admin.html', {'fornecedor': fornecedor, 'produtos' : page})


# @login_required
# def add_produto(request):

#     if request.method == 'POST':
#         form = ProdutoForm(request.POST, request.FILES)

#         if form.is_valid():
#             produto = form.save(commit=False)
#             produto.fornecedor = request.user.fornecedor
#             produto.slug = slugify(produto.titulo)
#             produto.save()
#             return redirect('fornecedor_admin')
#     else:
#         form = ProdutoForm()

#     return render(request,'add_produto.html', {'form' : form})

# @login_required
# def produto_edit(request, id):
#     produto = get_object_or_404(Produto, pk=id)
#     form = ProdutoForm(instance=produto)

#     if (request.method == 'POST'):
#         form = ProdutoForm(request.POST, instance=produto)

#         if form.is_valid():
#             produto.save()
#             return redirect('fornecedor_admin')
#         else:
#             return render(request, 'produto_edit.html', {'form': form, 'produto': produto})
#     else:
#         return render(request, 'produto_edit.html', {'form': form, 'produto': produto})



# @login_required
# def produto_delete(request, id):
#     produto = get_object_or_404(Produto, pk=id)
#     produto.delete()
#     messages.info(request,'Produto apagado')
#     return redirect('fornecedor_admin')
    