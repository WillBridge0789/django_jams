from rest_framework import serializers
from .models import *

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = [
            'id',
            'name',
            ]

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'bio',]

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'release_date',]

class SongsSerializer(serializers.ModelSerializer):
    # albums = AlbumSerializer(many=True)

    class Meta:
        model = Songs
        fields = ['name', 'duration',]