# Arquivo: meu_projeto/settings.py (NO TOPO)

import os 
from pathlib import Path
from dotenv import load_dotenv 
from django.urls import reverse_lazy 

load_dotenv() 

# CORREÇÃO CRÍTICA: BASE_DIR DEVE APONTAR PARA A RAIZ DO PROJETO (onde manage.py está)
BASE_DIR = Path(__file__).resolve().parent.parent 
# Agora, todos os caminhos subsequentes serão relativos a esta RAIZ.

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-t914bv7l_f#avz^=f^q2vo!9i(av5uf@c$o5spmd21oj9)(&ak')

# ...

DEBUG = os.environ.get('DEBUG', 'False') == 'True' 
if DEBUG:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
else:
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
    # WhiteNoise COMENTADO para o teste local
    # 'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
# STATIC_ROOT aponta para a pasta de coleta na raiz do projeto (um nível acima)
# Arquivo: meu_projeto/settings.py (NA SEÇÃO DE ARQUIVOS ESTÁTICOS)

# ...

STATIC_ROOT = Path(__file__).resolve().parent.parent / 'staticfiles'

# CORREÇÃO CRÍTICA: Diz ao Django para procurar na pasta 'static' na raiz
STATICFILES_DIRS = [
    # Esta é a localização correta do seu diretório 'static'
    Path(__file__).resolve().parent.parent / 'static', 
]

MEDIA_URL = '/media/'
# ...
# MEDIA_ROOT AGORA USA APENAS BASE_DIR
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
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