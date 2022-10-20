from django.urls import path
from .views import ClienteCreate, ClienteUpdate

urlpatterns = [
    path('cliente-form', ClienteCreate.as_view(), name='cliente-form'),
    path('cliente-update/<int:pk>/', ClienteUpdate.as_view(), name='cliente-update'),
    
]
