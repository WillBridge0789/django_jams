from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import Artist, Album, Songs, Genre, Playlist
from .serializers import (
    ArtistSerializer,
    AlbumSerializer,
    SongsSerializer,
    GenreSerializer,
    PlaylistSerializer,
)

# Create your views here.
#--------------------------------------------------------------------------------#
# def ArtistViewSet(request):
    # queryset = Artist.objects.all()
    # serializer_class = ArtistSerializer

# def AlbumViewSet(request):
    # queryset = Album.objects.all()
    # serializer_class = AlbumSerializer

# def SongsViewSet(request):
    # queryset = Songs.objects.all()
    # serializer_class = SongsSerializer

# def GenreViewSet(request):
    # queryset = Genre.objects.all()
    # serializer_class = GenreSerializer

# def PlaylistViewSet(request):
    # queryset = Playlist.objects.all()
    # serializer_class = PlaylistSerializer