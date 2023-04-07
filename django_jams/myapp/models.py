from django.db import models

# Create your models here.

class Album(models.Model):
     name = models.CharField(max_length=200)
     release_date = models.DateField()
     album_artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)
     songs = models.ManyToManyField('Songs')
     def __str__(self):
          return self.name

class Artist(models.Model):
     name = models.CharField(max_length=100, null=False)
     bio = models.TextField(max_length=500, null=True)
     albums = models.ManyToManyField('Album')
     songs = models.ManyToManyField('Songs')
     genres = models.ManyToManyField('Genres')
     def __str__(self):
          return self.albums

class Songs(models.Model):
     name = models.CharField(max_length=200)
     duration = models.DurationField()
     def __str__(self):
          return self.name

class Genres(models.Model):
     name = models.CharField(max_length=200)

     def __str__(self):
          return self.name


# class Playlist(models.Model):
#     name = models.CharField(max_length=200)