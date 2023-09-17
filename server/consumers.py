import asyncio
import psutil
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class CPUConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if message == 'get_cpu':
            cpu_percent = psutil.cpu_percent(interval=1)
            await self.send(text_data=json.dumps({
                'cpu_percent': cpu_percent
            }))