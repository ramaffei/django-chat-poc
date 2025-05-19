from django.urls import re_path
from django.urls.resolvers import URLPattern

from . import consumers

websocket_urlpatterns: list[URLPattern] = [
    re_path(r"ws/chat/(?P<room_id>\d+)/$", consumers.ChatConsumer.as_asgi()),
]
