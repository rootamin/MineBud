import asyncio
import psutil
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class SystemConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.connected = True
        await self.accept()
        self.task = asyncio.create_task(self.send_cpu_usage())

    async def disconnect(self, close_code):
        self.connected = False
        if self.task:
            self.task.cancel()

    async def receive(self, text_data):
        pass

    async def send_cpu_usage(self):
        while self.connected:
            cpu_percent = psutil.cpu_percent(interval=1)
            await self.send(text_data=json.dumps({
                'cpu_percent': cpu_percent
            }))
            await asyncio.sleep(1)  # sleep for 1 second
