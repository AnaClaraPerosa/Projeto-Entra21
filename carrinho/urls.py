from django.urls import path

from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('', views.carrinho_detalhe, name='carrinho'),
    path('sucesso/',views.sucesso,name='sucesso'),
]