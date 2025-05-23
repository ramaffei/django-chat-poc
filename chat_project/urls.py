"""
URL configuration for chat_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from chat import views

urlpatterns: list = [
    path('', views.IndexView.as_view(), name='index'),
    path('chat/<int:room_id>/', views.ChatRoomView.as_view(), name='chat_room'),
    path("api/", include("rooms.urls")),
    path("api/token/", obtain_auth_token, name="api_token_auth"),
]


if settings.ENVIRONMENT in ["Local", "DEV"]:
    urlpatterns += [path("admin/", admin.site.urls)]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
