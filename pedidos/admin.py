from django.contrib import admin
from .models import Itensped, Pedidos

# Register your models here.

admin.site.register(Pedidos)
admin.site.register(Itensped)