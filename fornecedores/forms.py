# from django.forms import ModelForm
# from produtos.models import Produto

from django import forms 
from .models import Fornecedores

class FornecedorForm(forms.ModelForm):

    class Meta:
        model = Fornecedores
        fields = ['fornecedor_nome', 'fornecedor_cnpj', 
            'fornecedor_email', 'fornecedor_telefone', 
            'fornecedor_logradouro', 'fornecedor_bairro',
            'fornecedor_numero', 'fornecedor_cep', 
            'fornecedor_complemento', 
            'fornecedor_obs', 'fornecedor_cidade']



# class ProdutoForm(ModelForm):
#     class Meta:
#         model = Produto 
#         fields = ['titulo','descricao','preco','imagem','categoria']
    