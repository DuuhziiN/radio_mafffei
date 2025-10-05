# Arquivo: meu_projeto/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.urls import path, include, re_path # NOVO IMPORT: re_path
from django.conf.urls import url # NOVO IMPORT: url
from django.views.static import serve # NOVO IMPORT: serve
urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs principais do aplicativo
    path('', include('radiomaffei.urls')), 
    # URLs de autenticação
    path('contas/', include('django.contrib.auth.urls')), 
]

# ==========================================================
# SOLUÇÃO FINAL: Mapeamento de Mídia e Estáticos no Servidor
# ==========================================================
# O Render executa essa lógica, garantindo que o WhiteNoise encontre os arquivos.

# 1. Mapeamento para MÍDIA (uploads de música) - CRÍTICO
# Isso resolve o erro Not Found, permitindo que o WhiteNoise sirva a pasta MEDIA.
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
    
# Mapeamento para ESTÁTICOS (CSS/JS)
urlpatterns += staticfiles_urlpatterns()