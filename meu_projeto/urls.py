# Arquivo: meu_projeto/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

urlpatterns = [
    path('admin/', admin.site.urls),
    # 1. URLs do Aplicativo
    path('', include('radiomaffei.urls')), 
    
    # 2. URLs de Autenticação (Login, Logout, etc.)
    path('contas/', include('django.contrib.auth.urls')), 
]

# Bloco para servir Estáticos e Mídia em desenvolvimento
if settings.DEBUG:
    # 1. Corrige o erro de MIME Type e carrega todos os arquivos estáticos
    urlpatterns += staticfiles_urlpatterns()
    
    # 2. Mapeamento para MÍDIA (uploads de música)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)