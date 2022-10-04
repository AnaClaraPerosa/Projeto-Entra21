from django.urls import path

from . import views

urlpatterns = [
    path('', views.carrinhho_detalhe, name='carrinho')
]