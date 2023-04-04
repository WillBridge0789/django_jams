from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'genre', views.GenreViewSet)
router.register(r'artist', views.ArtistViewSet)
router.register(r'album', views.AlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
