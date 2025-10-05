# Arquivo: meu_projeto/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # Importação necessária

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('radiomaffei.urls')), 
    path('contas/', include('django.contrib.auth.urls')), 
]

# ==========================================================
# SOLUÇÃO FINAL: Mapeamento de Mídia e Estáticos no Servidor
# ==========================================================

# Mapeamento para MÍDIA (uploads de música) - CRÍTICO
# Esta linha garante que o WhiteNoise/Django sirva os arquivos da pasta MEDIA.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# Mapeamento para ESTÁTICOS (CSS/JS) - Necessário para o modo DEBUG=False
urlpatterns += staticfiles_urlpatterns()