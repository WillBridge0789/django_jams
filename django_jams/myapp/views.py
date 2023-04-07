from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *

# Create your views here.
#--------------------------------------------------------------------------------#
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistReadOnlySerializer
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ArtistWriteSerializer
        else:
            return ArtistReadOnlySerializer



class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return AlbumWriteSerializer
        return AlbumReadOnlySerializer

class SongsViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
   
    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return SongsWriteSerializer
        return SongsReadOnlySerializer




class GenreViewSet(viewsets.ModelViewSet):
     queryset = Genres.objects.all()
     serializer_class = GenreSerializer

# def PlaylistViewSet(request):
    # queryset = Playlist.objects.all()
    # serializer_class = PlaylistSerializer