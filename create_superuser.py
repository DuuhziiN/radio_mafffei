# Arquivo: create_superuser.py

import os
import sys
import django
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured

# 1. Configurar o ambiente Django (CRÍTICO)
try:
    # Diz ao Django qual arquivo settings usar
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meu_projeto.settings')
    django.setup()
except ImproperlyConfigured:
    # Se o setup falhar por alguma razao, loga e sai
    print("Erro: DJANGO_SETTINGS_MODULE não configurado corretamente.")
    sys.exit(1)


# 2. Credenciais do Superusuário (Radialista)
# MUDE ESTES VALORES para algo seguro antes de subir!
USERNAME = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'radialista_admin')
EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@radio-maffei.com')
PASSWORD = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'sua_senha_segura_aqui')

User = get_user_model()

# 3. Criação do Usuário
if not User.objects.filter(username=USERNAME).exists():
    print(f"Criando Superusuário: {USERNAME}...")
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print("Superusuário criado com sucesso!")
else:
    print(f"Superusuário {USERNAME} já existe.")