from rest_framework.serializers import ModelSerializer
from .models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "name", "description", "created_at"]
        read_only_fields = ["id", "created_at"]
