# Arquivo: meu_projeto/asgi.py

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from radiomaffei.consumers import AudioConsumer # Ainda vamos criar isso

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meu_projeto.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        # Rota que o cliente vai usar para se conectar ao stream de voz
        path('ws/live_audio/', AudioConsumer.as_asgi()), 
    ]),
})