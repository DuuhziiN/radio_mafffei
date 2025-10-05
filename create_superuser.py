# Arquivo: create_superuser.py

import os
from django.contrib.auth import get_user_model

# Defina as credenciais do seu Superusuário. 
# MUDE ESTES VALORES para algo seguro antes de subir!
USERNAME = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'radialista_admin')
EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@radio-maffei.com')
PASSWORD = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'sua_senha_segura_aqui')

User = get_user_model()

# Tenta criar o Superusuário apenas se ele não existir
if not User.objects.filter(username=USERNAME).exists():
    print(f"Criando Superusuário: {USERNAME}...")
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print("Superusuário criado com sucesso!")
else:
    print(f"Superusuário {USERNAME} já existe.")