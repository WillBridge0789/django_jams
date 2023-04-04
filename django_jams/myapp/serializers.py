from rest_framework import serializers
from .models import *

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = [
            'name',
            ]

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'bio']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'release_date']