from rest_framework import serializers
from .models import *



#---Genre Serialiazers-----------------------------------------------------------------

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['id','name',]


#---Song Serialiazers-----------------------------------------------------------------

class SongsReadOnlySerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Songs
        fields = ['name', 'duration', 'genres']

class SongsWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['name', 'duration',]


#---Album Serialiazers-----------------------------------------------------------------

class AlbumWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'release_date', 'songs']

class AlbumReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'release_date', 'songs']

#---Artist Serialiazers-----------------------------------------------------------------

class ArtistWriteSerializer(serializers.ModelSerializer):
    albums = AlbumWriteSerializer(many=True)
    songs = SongsWriteSerializer(many=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'albums', 'songs', 'genres']

class ArtistReadOnlySerializer(serializers.ModelSerializer):
    albums = AlbumReadOnlySerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'albums', 'songs', 'genres']


