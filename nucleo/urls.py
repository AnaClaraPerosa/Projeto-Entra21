from django.urls import path
from . import views
from django.views.generic import TemplateView



urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('depoimentos/',views.depoimentos, name='depoimentos'),
    path('loja/',views.loja, name= 'loja'),
]