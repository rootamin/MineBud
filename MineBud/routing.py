import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from server import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MineBud.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("ws/system/", consumers.SystemConsumer.as_asgi()),
        path("ws/console/", consumers.ConsoleConsumer.as_asgi()),
    ]),
})