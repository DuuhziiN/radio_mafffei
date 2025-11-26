# ARQUIVO: radiomaffei/consumers.py

import json # Importa o módulo JSON para lidar com comandos de texto
from channels.generic.websocket import AsyncWebsocketConsumer

class AudioConsumer(AsyncWebsocketConsumer):
    # CRÍTICO: Variável de controle para garantir que o cliente está pronto.
    is_ready_to_send = False 
    
    async def connect(self):
        self.group_name = 'live_audio_group'
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        
        # NOTA: Não inicie o envio de áudio aqui. Ele será iniciado pelo 'receive' do cliente.
        print(f"Novo cliente conectado ao grupo: {self.group_name}")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        print(f"Cliente desconectado do grupo: {self.group_name}")

    # A função receive precisa lidar com dados de áudio (bytes) E comandos de controle (texto).
    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            # Lógica para comandos do cliente (como o 'ready_to_receive' do JavaScript)
            try:
                data = json.loads(text_data)
                command = data.get('command')
                
                # NOVO: Se o cliente envia "ready_to_receive", habilitamos o envio para este cliente
                if command == 'ready_to_receive':
                    self.is_ready_to_send = True
                    print(f"Cliente {self.channel_name} pronto para receber áudio.")
                    
            except json.JSONDecodeError:
                print(f"Recebido texto não JSON: {text_data}")

        if bytes_data:
            # Lógica para envio de áudio (Radialista enviando)
            print(f"Recebendo {len(bytes_data)} bytes do áudio. Repassando...")

            # O group_send envia o áudio para TODOS, incluindo o radialista, mas o filtro será no audio_message
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'audio.message',
                    'audio_data': bytes_data 
                }
            )

    # Função que envia o áudio para os ouvintes
    async def audio_message(self, event):
        # CRÍTICO: Só envia o áudio para o cliente se ele estiver pronto
        if self.is_ready_to_send:
            await self.send(bytes_data=event['audio_data'])
        else:
            # Opcional: Ignora o áudio até que o cliente avise que o MediaSource está aberto
            # Isso impede que o browser do cliente acumule pacotes perdidos, resolvendo o problema de sincronização.
            pass