"""
Django settings for meu_projeto project.
"""

# =================================================================
# CORREÇÃO CRÍTICA: CARREGAMENTO DE VARIÁVEIS DE AMBIENTE (.env)
# MOVEMOS PARA O TOPO para garantir que as chaves existam antes da configuração do Django.
# =================================================================
import os 
from pathlib import Path
from dotenv import load_dotenv 
from django.urls import reverse_lazy 

load_dotenv() # <--- CARREGA O ARQUIVO .env AQUI

BASE_DIR = Path(__file__).resolve().parent.parent

# A SECRET_KEY agora puxa do ambiente
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-t914bv7l_f#avz^=f^q2vo!9i(av5uf@c$o5spmd21oj9)(&ak')

DEBUG = True 
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'radiomaffei',
    'channels',
    'cloudinary_storage', 
    'cloudinary', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meu_projeto.urls'

# Configuração para encontrar a pasta templates/registration/ na raiz
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS CORRIGIDO: Usa o método os.path.join para compatibilidade universal
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
        'NAME': BASE_DIR / 'db.sqlite3',
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
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# CONFIGURAÇÃO DE CREDENCIAIS (Puxa do .env)
CLOUDINARY_CLOUD_NAME = os.environ.get('CLOUDINARY_CLOUD_NAME')
CLOUDINARY_API_KEY = os.environ.get('CLOUDINARY_API_KEY')
CLOUDINARY_API_SECRET = os.environ.get('CLOUDINARY_API_SECRET')

# Configura o Django para usar o Cloudinary para a MÍDIA
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
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