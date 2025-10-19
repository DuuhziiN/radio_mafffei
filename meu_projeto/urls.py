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
# SOLUÇÃO FINAL DE URL PARA AMBIENTE DE DESENVOLVIMENTO (DEBUG=True)
# ==========================================================
# Arquivo: meu_projeto/urls.py (NO FINAL)


# Removida a importação de staticfiles_urlpatterns para simplificar

if settings.DEBUG:
    # 1. Mapeamento para MÍDIA
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # 2. Mapeamento ESTÁTICO DIRETO: Usa a pasta STATICFILES_DIRS (o caminho que acabamos de configurar)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])