from django.conf import settings

from produtos.models import Produto

class Carrinho(object):
    def __init__(self, request):
        self.session = request.session
        carrinho = self.session.get(settings.CART_SESSION_ID)

        if not carrinho:
            carrinho = self.session[settings.CART_SESSION_ID] = {}

        self.carrinho = carrinho

    def __iter__(self):
        for p in self.carrinho.keys():
            self.carrinho[str(p)]['produto'] = Produto.objects.get(pk=p)
        
        for item in self.carrinho.values():
            item['preco_total'] = item['produto'].preco * item['quantidade']

            yield item
        
    def __len__(self):
        return sum(item['quantidade'] for item in self.carrinho.values())

    def add(self, produto_id, quantidade=1, update_quantidade=False):
        produto_id = str(produto_id)

        if produto_id not in self.carrinho:
            self.carrinho[produto_id] = {'quantidade' : 1, 'id' : produto_id}

        if update_quantidade:
            self.carrinho[produto_id] ['quantidade'] += int(quantidade)

            if self.carrinho[produto_id] ['quantidade'] == 0:
                self.remove(produto_id)

        self.save()
    
    def remove(self, produto_id):
        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.carrinho
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_custo_total(self):
        for p in self.carrinho.keys():
            self.carrinho[str(p)]['produto'] = Produto.objects.get(pk=p)

        return sum(item['quantidade'] * item['produto'].preco for item in self.carrinho.values())