from django.urls import path
from . import views
from django.views.generic import TemplateView



urlpatterns = [
    path('', views.index, name='index'),
    path('depoimentos/',views.depoimentos, name='depoimentos'),
    path('loja/',views.loja, name= 'loja'),
    path('pagamento/',views.pagamento, name= 'pagamento'),
]