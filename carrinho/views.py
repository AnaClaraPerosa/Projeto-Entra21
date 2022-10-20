from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido, ItemPedido
from clientes.models import Clientes
from .carrinho import Carrinho
from django.contrib import messages
from django.shortcuts import render, redirect
import json


# Create your views here.


@csrf_exempt
@login_required
def carrinho_detalhe(request):

    print("Entrou aqui na view Carrinho")
    carrinho = Carrinho(request)

    cli = Clientes.objects.filter(usuario_id=request.user.id)

    if(cli):
        print("cliente existe")
        novocliente = False

    else:
        print("Cliente NÃOOOOOO EXISTE")
        novocliente = True

    if request.method == 'POST':
        print( " entrou com post ")
        

        if (cli):
            for x in cli.values():
                newped = Pedido(
                    primeiro_nome=x["cliente_nome"],
                    email=x["cliente_email"],
                    endereco=x["cliente_logradouro"],
                    cep=x["cliente_cep"],
                    cidade=x["cliente_cidade_id_id"],
                    telefone=x["cliente_telefone"],
                    valor_total=carrinho.get_custo_total(),
                    quant_paga=1
                )


            newped.save()

####################### salvar itens do pedido ###############
            for x in carrinho:
                newitemsped = ItemPedido(
                    pedido = newped,
                    produto = x['produto'],
                    fornecedor = x['produto'].fornecedor,
                    preco = x['produto'].preco,
                    quantidade = x['quantidade']
                )

                newped.fornecedores.add(x['produto'].fornecedor)


            newitemsped.save()

            carrinho.clear()   
            data = { 'valor_total' : newped.valor_total }         
            return render(request, 'sucesso.html', 
                    {   'CLI': json.dumps(cli,   default=str),
                        'DATA' : json.dumps(data, default=str)
                    }
                )

        else:
            print("cadiu no else")
            return render(request, 'sucesso.html', 
                {   'CLI': json.dumps(cli,   default=str)
                }
            )       


    remove_do_carrinho = request.GET.get('remove_do_carrinho', '')
    muda_quantidade = request.GET.get('muda_quantidade', '')
    quantidade = request.GET.get('quantidade', 0)

    if remove_do_carrinho:
        carrinho.remove(remove_do_carrinho)
        return redirect('carrinho')

    if muda_quantidade:
        carrinho.add(muda_quantidade, quantidade, True)
        return redirect('carrinho')


    return render(request, 'carrinho.html',
        { 
            'NOVOCLIENTE' : novocliente,
            'CLIENTE'     : cli
        }
    )