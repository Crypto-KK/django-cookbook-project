from django.contrib import admin

from .models import Genre, Director, Actor, Movie

admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Movie)