from django.urls import path
from django.contrib.auth import views as auth_views
# from . import views

from .views import FornecedorCreate, FornecedorUpdate, FornecedorDelete, FornecedorList

urlpatterns = [
    # path('seja_fornecedor/', views.seja_fornecedor, name='seja_fornecedor'),
    # path('fornecedor_admin/', views.fornecedor_admin, name='fornecedor_admin'),
    # path('add_produto/',views.add_produto, name='add_produto'),
    # path('produto_edit/<int:id>', views.produto_edit, name="produto_edit"),
    # path('produto_delete/<int:id>', views.produto_delete, name="produto_delete"),
    
    path('fornecedor-form', FornecedorCreate.as_view(), name='fornecedor-form'),
    path('fornecedor-update/<int:pk>/', FornecedorUpdate.as_view(), name='fornecedor-update'),
    path('fornecedor-delete/<int:pk>/', FornecedorDelete.as_view(), name='fornecedor-delete'),
    path('fornecedor-list/', FornecedorList.as_view(), name='fornecedor-list'),
] 