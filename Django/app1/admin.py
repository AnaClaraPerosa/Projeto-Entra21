from django.contrib import admin
from .models import Cidades, Clientes, Fornecedores, Itensped, Pedidos, Produtos, Segmentos

# Register your models here.

admin.site.register(Fornecedores)
admin.site.register(Clientes)
admin.site.register(Cidades)
admin.site.register(Segmentos)
admin.site.register(Produtos)
admin.site.register(Pedidos)
admin.site.register(Itensped)