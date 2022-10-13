from django.contrib import admin

# Register your models here.

from .models import DepoimentoGeral


@admin.register(DepoimentoGeral)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'depoimento')

