from django.db.models.manager import BaseManager
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from chat_project.authentication import BearerTokenAuthentication

from .models import Room
from .serializers import RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset: BaseManager[Room] = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = [BearerTokenAuthentication]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminUser()]
        return [AllowAny()]
