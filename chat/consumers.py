import json
import logging

from asgiref.sync import sync_to_async
from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer

from rooms.models import Room

from .redis import add_user_to_room, remove_user_from_room

logger = logging.getLogger(__name__)


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self) -> None:
        self.room_id: str = self.scope["url_route"]["kwargs"]["room_id"]
        self.username: str | None = None

        # Verificar que la sala con ese ID existe
        self.room: Room | None = await self.get_room(int(self.room_id))
        if not self.room:
            raise DenyConnection()

        self.room_group_name: str = f"chat_{self.room.id}"

        await self.accept()

    async def disconnect(self) -> None:
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        if self.username:
            await remove_user_from_room(self.room_id, self.username)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat.leave",
                    "username": self.username,
                },
            )

    # Receive message from WebSocket
    async def receive(self, text_data: str) -> None:
        data: dict = json.loads(text_data)
        message: str | None = data.get("message")

        if not message:
            return

        # Esperamos el primer mensaje de tipo 'init'
        if not self.username:
            if data.get("type") != "init" or not data.get("username"):
                await self.close(code=4001)
                return

            self.username = data["username"]
            try:
                await add_user_to_room(self.room_id, self.username)
                await self.channel_layer.group_add(
                    self.room_group_name, self.channel_name
                )
            except Exception as e:
                await self.close(code=4002)
                logger.error(
                    f"Error al agregar el usuario {self.username} a la sala {self.room_id}: {e}"
                )
                return

            # Notificamos a otros
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat.join",
                    "username": self.username,
                },
            )

        if data.get("type") == "chat_message":
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "message": message,
                    "username": self.username,
                },
            )

    # Receive message from room group
    async def chat_message(self, event: dict[str]) -> None:
        await self.send(
            text_data=json.dumps(
                {
                    "type": "message",
                    "message": event["message"],
                    "username": event["username"],
                }
            )
        )

    async def chat_join(self, event: dict[str]) -> None:
        await self.send(
            text_data=json.dumps(
                {
                    "type": "message",
                    "message": f"{event['username']} se unió al chat",
                    "username": event["username"],
                }
            )
        )

    async def chat_leave(self, event: dict[str]) -> None:
        await self.send(
            text_data=json.dumps(
                {
                    "type": "message",
                    "message": f"{event['username']} se fue del chat",
                    "username": event["username"],
                }
            )
        )

    @sync_to_async
    def get_room(self, room_id: int) -> Room | None:
        try:
            return Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return None
