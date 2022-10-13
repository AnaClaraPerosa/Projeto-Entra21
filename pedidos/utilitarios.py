from carrinho.carrinho import Carrinho

from .models import Pedido , ItemPedido

def checkout(request, primeiro_nome, sobrenome, email, endereco, cep, cidade, telefone, valor):
    pedido = Pedido.objects.create(
        primeiro_nome = primeiro_nome,
        sobrenome = sobrenome,
        email = email,
        endereco = endereco,
        cep = cep,
        cidade = cidade,
        telefone = telefone,
        quant_paga = valor
    )

    for item in Carrinho(request):
        ItemPedido.objects.create(
            pedido = pedido,
            produto = item['produto'],
            fornecedor = item['produto'].fornecedor,
            preco = item['produto'].preco,
            quantidade = item['quantidade']
        )

        pedido.fornecedores.add(item['produto'].fornecedor)

    return pedido