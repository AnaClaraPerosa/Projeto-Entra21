from django.urls import path

from . import views

urlpatterns = [
    path('', views.carrinho_detalhe, name='carrinho'),
    path('sucesso/',views.sucesso,name='sucesso'),
]