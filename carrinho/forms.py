from django import forms

class CheckoutForm(forms.Form):
    primeiro_nome = forms.CharField(max_length=255)
    sobrenome = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    primeiro_nome = forms.CharField(max_length=255)
    telefone = forms.CharField(max_length=255)
    endereco = forms.CharField(max_length=255)
    cep = forms.CharField(max_length=255)
    cidade = forms.CharField(max_length=255)
    # stripe_token = forms.CharField(max_length=255)1