from django.urls import path

from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('', views.carrinhho_detalhe, name='carrinho'),

]