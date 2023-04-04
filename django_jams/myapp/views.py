from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *

# Create your views here.
#--------------------------------------------------------------------------------#
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

# def SongsViewSet(request):
    # queryset = Songs.objects.all()
    # serializer_class = SongsSerializer

class GenreViewSet(viewsets.ModelViewSet):
     queryset = Genres.objects.all()
     serializer_class = GenreSerializer

# def PlaylistViewSet(request):
    # queryset = Playlist.objects.all()
    # serializer_class = PlaylistSerializer