from django.urls import path
from .views import ClienteCreate, ClienteUpdate, ClienteDelete, ClienteList

urlpatterns = [
    path('cliente-form', ClienteCreate.as_view(), name='cliente-form'),
    path('cliente-update/<int:pk>/', ClienteUpdate.as_view(), name='cliente-update'),
    path('cliente-delete/<int:pk>/', ClienteDelete.as_view(), name='cliente-delete'),
    path('cliente-list/', ClienteList.as_view(), name='cliente-list'),
]
