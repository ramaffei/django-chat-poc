from rest_framework import permissions, viewsets

from .models import Room
from .serializers import RoomSerializer


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permite acceso completo solo a administradores. Los demás solo pueden leer.
    """

    def has_permission(self, request, view):
        # SAFE_METHODS = GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly]
