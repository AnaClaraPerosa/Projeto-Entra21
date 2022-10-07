# import stripe

# from django.conf import settings
# from django.contrib import messages
from django.shortcuts import render,redirect

# from.forms import CheckoutForm
from .carrinho import Carrinho


# from app5.utilitarios import checkout

# Create your views here.


def carrinhho_detalhe(request):
    carrinho = Carrinho(request)

    # if request.method == 'POST':
    #     form = CheckoutForm(request.POST)

    #     if form.is_valid():
    #         stripe.api_key = settings.STRIPE_SECRET_KEY

    #         stripe_token = form.cleaned_data['stripe_token']

    #         carrega = stripe.Charge.create(
    #             valor = int(carrinho.get_custo_total() * 100),
    #             moeda = 'BRL',
    #             descricao = 'Cobrança da loja',
    #             fonte = stripe_token
    #         )

    #         primeiro_nome = form.cleaned_data['primeiro_nome']
    #         sobrenome = form.cleaned_data['sobrenome']
    #         email = form.cleaned_data['email']
    #         telefone = form.cleaned_data['telefone']
    #         endereco = form.cleaned_data['endereco']
    #         cep = form.cleaned_data['cep']
    #         cidade = form.cleaned_data['cidade']

    #         pedido = checkout(request, primeiro_nome, sobrenome, email, telefone, endereco, cep, cidade, carrinho.get_custo_total())

    #         carrinho.clear()

    #         return redirect('sucesso')
    # else:
    #     form = CheckoutForm()

    remove_do_carrinho = request.GET.get('remove_do_carrinho','')
    muda_quantidade = request.GET.get('muda_quantidade','')
    quantidade = request.GET.get('quantidade',0)

    if remove_do_carrinho:
        carrinho.remove(remove_do_carrinho)

        return redirect('carrinho')

    if muda_quantidade:
        carrinho.add(muda_quantidade, quantidade, True)

        return redirect('carrinho')
    
    return render(request, 'carrinho.html')

# def sucesso(request):
#      return render(request, 'sucesso.html')


