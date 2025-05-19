from django.urls import include, path
from django.urls.resolvers import URLResolver
from rest_framework.routers import DefaultRouter

from .views import RoomViewSet

router = DefaultRouter()
router.register(r"rooms", RoomViewSet, basename="room")

urlpatterns: list[URLResolver] = [
    path("", include(router.urls)),
]
