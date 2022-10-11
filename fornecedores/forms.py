from django.forms import ModelForm

from produtos.models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto 
        fields = ['titulo','descricao','preco','imagem','categoria']
    