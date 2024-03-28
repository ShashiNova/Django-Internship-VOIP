from django.contrib import admin
from .models import Song, Playlist, Profile

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Profile)
