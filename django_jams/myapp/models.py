from django.db import models

# Create your models here.
class Artist(models.Model):
     name = models.CharField(max_length=100, null=False)
     bio = models.TextField(max_length=500, null=True)
#     image = models.URLField(null=True)

class Album(models.Model):
     name = models.CharField(max_length=200)
     release_date = models.DateField()
#     cover_art = models.URLField(null=True)

class Songs(models.Model):
     name = models.CharField(max_length=200)
     duration = models.CharField(max_length=100, null=False)
#     cover_art = models.URLField(null=True)

class Genres(models.Model):
     name = models.CharField(max_length=200)
     genre = models.ManyToManyField("Artist")

# class Playlist(models.Model):
#     name = models.CharField(max_length=200)