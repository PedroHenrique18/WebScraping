from django.urls import path
from . import views

urlpatterns = [
    path('lista_urls/', views.lista_urls, name='lista_urls'),
    path('cadastrar_url/', views.cadastrar_url, name='cadastrar_url'),
    path('raspagem_dados/', views.raspagem_dados, name='raspagem_dados'),
]
