# Arquivo: meu_projeto/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.views.static import serve as static_serve
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('radiomaffei.urls')), 
    path('contas/', include('django.contrib.auth.urls')), 
]

# ==========================================================
# SOLUÇÃO FINAL DE URL PARA AMBIENTE DE PRODUÇÃO/DEV
# O Render precisa desta lógica unificada
# ==========================================================
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

# 2. MAPEAMENTO CRÍTICO PARA MÍDIA (FORA DO BLOCO DEBUG PARA PRODUÇÃO)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', static_serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]