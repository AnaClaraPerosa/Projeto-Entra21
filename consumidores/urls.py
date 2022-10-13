from django.urls import path
from .views import ConsumidorCreate, ConsumidorUpdate, ConsumidorDelete, ConsumidorList
from . import views

urlpatterns = [
    path('consumidor-form', ConsumidorCreate.as_view(), name='consumidor-form'),
    path('consumidor-update/<int:pk>/', ConsumidorUpdate.as_view(), name='consumidor-update'),
    path('consumidor-delete/<int:pk>/', ConsumidorDelete.as_view(), name='consumidor-delete'),
    path('consumidor-list/', ConsumidorList.as_view(), name='consumidor-list'),]
