import asyncio
import psutil
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
import json, threading
from .minecraft import process


class SystemConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.connected = True
        await self.accept()
        self.task = asyncio.create_task(self.send_system_usage())

    async def disconnect(self, close_code):
        self.connected = False
        if self.task:
            self.task.cancel()

    async def receive(self, text_data):
        pass

    async def send_system_usage(self):
        old_value = psutil.net_io_counters(pernic=False)
        while self.connected:
            # CPU
            cpu_percent = psutil.cpu_percent(interval=1)

            # Storage
            partitions = psutil.disk_partitions()

            total_space = 0
            used_space = 0
            for partition in partitions:
                usage = psutil.disk_usage(partition.mountpoint)
                total_space += usage.total
                used_space += usage.used

            total_space_gb = "{:.2f}".format(total_space / (1024 ** 3))
            used_space_gb = "{:.2f}".format(used_space / (1024 ** 3))
            used_space_raw = float(used_space_gb) / float(total_space_gb) * 100
            used_space_percentage = "{:.0f}".format(used_space_raw)

            # Network
            new_value = psutil.net_io_counters(pernic=False)
            sent_diff = new_value.bytes_sent - old_value.bytes_sent
            recv_diff = new_value.bytes_recv - old_value.bytes_recv
            sent_diff_mb = round(sent_diff / (1024 ** 2), 2)
            recv_diff_mb = round(recv_diff / (1024 ** 2), 2)
            total_sent = "{:.2f}".format(new_value.bytes_sent / (1024 ** 3))
            total_recv = "{:.2f}".format(new_value.bytes_recv / (1024 ** 3))

            await self.send(text_data=json.dumps({
                'cpu_percent': cpu_percent,
                'total_space': total_space_gb,
                'used_space': used_space_gb,
                'used_space_percentage': used_space_percentage,
                'bandwidth_sent': sent_diff_mb,
                'bandwidth_received': recv_diff_mb,
                'total_sent': total_sent,
                'total_recv': total_recv,
            }))

            old_value = new_value

            await asyncio.sleep(1)  # sleep for 1 second


class ConsoleConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        if process:
            threading.Thread(target=self.send_output).start()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        if process:
            process.stdin.write(text_data.encode())
            process.stdin.flush()

    def send_output(self):
        for line in iter(process.stdout.readline, b''):
            self.send(line.decode())
