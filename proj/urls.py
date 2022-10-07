"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('nucleo.urls')),
    path('carrinho/',include('carrinho.urls')),
    path('clientes/',include('clientes.urls')),        
    # path('depoimentos/',include('depoimentos.urls')),
    path('endereco/',include('endereco.urls')),
    path('fornecedores/',include('fornecedores.urls')),
    path('produtos/',include('produtos.urls')),    
    path('usuarios/',include('usuarios.urls')),
    # path('pagamento/',include('pagamento.urls')),
 ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
