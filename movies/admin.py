from django.contrib import admin
from .models import Director, Movie, Genre

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Genre)


