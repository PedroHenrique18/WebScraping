from django.urls import path
from django.contrib import admin
from webscraping import views

urlpatterns = [
    path('admin/', admin.site.urls),  # URL padrão de administração do Django
    path('lista_urls/', views.lista_urls, name='lista_urls'),  # URL personalizada para sua view
    path('cadastrar_url/', views.cadastrar_url, name='cadastrar_url'),
    path('raspagem_dados/', views.raspagem_dados, name='raspagem_dados'),
]
