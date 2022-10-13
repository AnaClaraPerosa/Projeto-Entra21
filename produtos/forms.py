from django import forms

class AddNoCarrinhoForm(forms.Form):
    quantidade = forms.IntegerField()