from django.urls import path
from . import views

# O 'app_name' é crucial para usar o namespace radiomaffei:
app_name = 'radiomaffei' 

urlpatterns = [
    # 1. Página Inicial / Ouvinte
    path('', views.pagina_ouvinte, name='home'), 
    
    # 2. Página do Radialista (restrita)
    path('radialista/', views.pagina_radialista, name='radialista'),
    
    # 3. Rota para Deletar Música (aceita o ID da música)
    path('deletar/<int:musica_id>/', views.deletar_musica, name='deletar_musica'),
    path('programacao/', views.programacao, name='programacao'),
    path('sobre/', views.sobre_nos, name='sobre_nos'),
    path('equipe/', views.equipe, name='equipe'),
    path('midias/', views.midias, name='midias'),
    path('concursos/', views.concursos, name='concursos'),
]