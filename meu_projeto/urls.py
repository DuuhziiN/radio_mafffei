# Arquivo: meu_projeto/urls.py

from django.contrib import admin
# Importamos re_path para o mapeamento de arquivos em vez da antiga url
from django.urls import path, include, re_path 
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Importamos 'serve' para servir a pasta MEDIA com o re_path
from django.views.static import serve 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('radiomaffei.urls')), 
    path('contas/', include('django.contrib.auth.urls')), 
]

# ==========================================================
# SOLUÇÃO FINAL DE URL PARA AMBIENTE DE PRODUÇÃO (RENDER)
# ==========================================================

# 1. Mapeamento para MÍDIA (uploads de música) - CRÍTICO
# Usa re_path para o mapeamento direto de arquivos, a única forma que funciona em produção
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
    
# 2. Mapeamento para ESTÁTICOS (CSS/JS)
urlpatterns += staticfiles_urlpatterns()