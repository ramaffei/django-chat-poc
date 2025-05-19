from django.db.models.manager import BaseManager
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from rooms.models import Room


class IndexView(View):
    template_name: str = "index.html"

    def get(self, request) -> HttpResponse:
        rooms: BaseManager[Room] = Room.objects.all()
        return render(request, self.template_name, {"rooms": rooms})


class ChatRoomView(View):
    template_name = "chat_room.html"

    def get(self, request, room_id) -> HttpResponse:
        room: Room = get_object_or_404(Room, id=room_id)
        return render(request, self.template_name, {"room": room})
