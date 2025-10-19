# Arquivo: meu_projeto/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('radiomaffei.urls')), 
    path('contas/', include('django.contrib.auth.urls')), 
]

# ==========================================================
# SOLUÇÃO FINAL: Mapeamento de Mídia e Estáticos
# ==========================================================

# Mapeamento ESTÁTICO (CSS/JS) - Usado em desenvolvimento e coletado em produção
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

# Mapeamento CRÍTICO para MÍDIA (uploads de música) - DEVE SER ATIVO EM PRODUÇÃO
# Esta linha garante que o WhiteNoise/Django sirva a pasta MEDIA.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)