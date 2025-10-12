# Arquivo: meu_projeto/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
# Removida a importação de staticfiles_urlpatterns para evitar conflitos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('radiomaffei.urls')), 
    path('contas/', include('django.contrib.auth.urls')), 
]

# ==========================================================
# SOLUÇÃO FINAL DE URL PARA AMBIENTE DE PRODUÇÃO/DEV
# ==========================================================

# Mapeamento para MÍDIA (uploads de música) - Necessário em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# EM PRODUÇÃO (RENDER), O WHITE NOISE NO MIDDLEWARE ASSUME TODOS OS ARQUIVOS ESTÁTICOS