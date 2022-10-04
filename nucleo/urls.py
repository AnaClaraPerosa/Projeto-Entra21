from django.urls import path
from . import views
from django.views.generic import TemplateView



urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('loja/',views.loja, name= 'loja'),
    
]