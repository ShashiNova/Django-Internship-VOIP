from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    duration = models.DurationField()
    file = models.FileField(upload_to='songs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    songs = models.ManyToManyField('Song', related_name='playlists', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    playlists = models.ManyToManyField('Playlist', related_name='users', blank=True)

    def __str__(self):
        return self.user.username
