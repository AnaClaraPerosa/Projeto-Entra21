from django.urls import path
from .views import ClienteCreate, ClienteUpdate

urlpatterns = [
    path('cadastrar/cliente', ClienteCreate.as_view(), name='cadastar-cliente'),
    path('editar/cliente/<int:pk>/', ClienteUpdate.as_view(), name='editar-cliente'),
    # path('deletar/clientes/<int:pk>/', ClienteDelete.as_view(), name='deletar-cliente'),
    # path('listar/cliente/', ClienteList.as_view(), name='listar-cliente'),
]
