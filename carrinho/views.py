from django.contrib import messages
from django.shortcuts import render,redirect

from.forms import CheckoutForm
from .carrinho import Carrinho
# from clientes.models import Clientes
from pedidos.utilitarios import checkout

# Create your views here.


def carrinho_detalhe(request):
    carrinho = Carrinho(request)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        if form.is_valid():
            # cliente = Clientes.objects.filter(id=form.request.user.id)
            primeiro_nome = form.cleaned_data['primeiro_nome']
            sobrenome = form.cleaned_data['sobrenome']
            email = form.cleaned_data['email']
            endereco = form.cleaned_data['endereco']
            cep = form.cleaned_data['cep']
            cidade = form.cleaned_data['cidade']
            telefone = form.cleaned_data['telefone']

            pedido = checkout(request, primeiro_nome, sobrenome, email, endereco, cep, cidade, telefone, carrinho.get_custo_total())

            carrinho.clear()

            return redirect('sucesso')
    else:
        form = CheckoutForm()

    remove_do_carrinho = request.GET.get('remove_do_carrinho','')
    muda_quantidade = request.GET.get('muda_quantidade','')
    quantidade = request.GET.get('quantidade',0)

    if remove_do_carrinho:
        carrinho.remove(remove_do_carrinho)

        return redirect('carrinho')

    if muda_quantidade:
        carrinho.add(muda_quantidade, quantidade, True)

        return redirect('carrinho')
    
    return render(request, 'carrinho.html',{'form' : form})


def sucesso(request):
     return render(request, 'sucesso.html')