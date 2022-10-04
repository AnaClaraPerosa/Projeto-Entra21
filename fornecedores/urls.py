from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('seja_fornecedor/', views.seja_fornecedor, name='seja_fornecedor'),
    path('fornecedor_admin/', views.fornecedor_admin, name='fornecedor_admin'),
    path('add_produto/',views.add_produto, name='add_produto'),
    path('produto_edit/<int:id>', views.produto_edit, name="produto_edit"),
    path('produto_delete/<int:id>', views.produto_delete, name="produto_delete"),
    
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('login/', auth_views.LoginView.as_view(template_name ='login.html'), name='login')
] 