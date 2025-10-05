# Arquivo: radiomaffei/consumers.py

from channels.generic.websocket import AsyncWebsocketConsumer # Mudei para AsyncWebsocketConsumer

class AudioConsumer(AsyncWebsocketConsumer): # Mudei a classe base para Async
    async def connect(self):
        self.group_name = 'live_audio_group'
        
        # O group_add agora é assíncrono e precisa de await
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept() # O accept também precisa de await
        print(f"Novo cliente conectado ao grupo: {self.group_name}")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        print(f"Cliente desconectado do grupo: {self.group_name}")

    # A função receive precisa ser assíncrona para lidar com a comunicação
    async def receive(self, bytes_data):
        # Este print agora deve aparecer no terminal!
        print(f"Recebendo {len(bytes_data)} bytes do áudio. Repassando...")

        # O group_send é assíncrono e crucial para o broadcast
        await self.channel_layer.group_send(
            self.group_name, # É aqui que o áudio é enviado para TODOS no grupo!
            {
                'type': 'audio.message',
                'audio_data': bytes_data 
            }
        )

    # Função que envia o áudio para os ouvintes
    async def audio_message(self, event):
        # Pegamos o dado do dicionário 'event'
        await self.send(bytes_data=event['audio_data'])