from django.shortcuts import render

# Create your views here.

def helloworld(request):
    versao = 'Olá mundo'
    return render(request, 'about.html',
        {'data': versao}
    )
