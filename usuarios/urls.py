from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PerfilComplemento, PerfilCreate,PerfilUpdate

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name ='login.html'), name='login'),
    path('registre-se/', PerfilCreate.as_view(), name='registre-se'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('atualizar-dados/', PerfilUpdate.as_view(), name='atualizar-dados'),
    path('cadastro/',PerfilComplemento.as_view(), name='cadastro')
]
