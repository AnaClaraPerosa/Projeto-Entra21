from django.urls import path

from . import views

urlpatterns = [
    path('pesquisa/',views.pesquisa, name='pesquisa'),
    path('<slug:categoria_slug>/<slug:produto_slug>/', views.produto, name='produto'),
    path('<slug:categoria_slug>/', views.categoria, name='categoria')
]