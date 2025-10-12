"""
Django settings for meu_projeto project.
"""

import os 
from pathlib import Path
from dotenv import load_dotenv 
from django.urls import reverse_lazy 

# Carrega variáveis de ambiente
load_dotenv() 

# BASE_DIR aponta para o diretório de configurações.
BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-t914bv7l_f#avz^=f^q2vo!9i(av5uf@c$o5spmd21oj9)(&ak')

# Lógica de DEBUG e ALLOWED_HOSTS para produção
DEBUG = os.environ.get('DEBUG', 'False') == 'True' 
if DEBUG:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
else:
    # Em produção (Render), aceita a URL pública
    ALLOWED_HOSTS = ['radio-mafffei.onrender.com', '*'] 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'radiomaffei',
    'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # CRÍTICO: WhiteNoise DEVE estar ativo para servir arquivos em produção
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CSRF_TRUSTED_ORIGINS = [
    'https://radio-mafffei.onrender.com',
    'https://*.onrender.com', # Adicionado para cobrir subdomínios do Render
]
ROOT_URLCONF = 'meu_projeto.urls'

# DIRS aponta para a pasta templates/ ao lado de settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ASGI_APPLICATION = 'meu_projeto.asgi.application' 


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # Banco de dados na raiz do projeto (um nível acima)
        'NAME': Path(__file__).resolve().parent.parent / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Configurações de Arquivos Estáticos e Mídia
STATIC_URL = '/static/'
# STATIC_ROOT DEVE APONTAR PARA A PASTA DE COLETA NA RAIZ DO PROJETO
STATIC_ROOT = Path(__file__).resolve().parent.parent / 'staticfiles'

# CORREÇÃO CRÍTICA: Diz ao Django para procurar na pasta 'static' da raiz
STATICFILES_DIRS = [
    Path(__file__).resolve().parent.parent / 'static', 
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(Path(__file__).resolve().parent.parent, 'media')


# Arquivo: meu_projeto/settings.py (NA SEÇÃO STORAGES)

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    # SOLUÇÃO FINAL: Usa o StaticFilesStorage simples para evitar o erro "Missing manifest"
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

# Configuração de Login e Logout
LOGIN_REDIRECT_URL = reverse_lazy('radiomaffei:radialista') 
LOGOUT_REDIRECT_URL = reverse_lazy('radiomaffei:home')