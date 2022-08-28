from django.db import models


class Director(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return'%s, %s' % (self.first_name, self.last_name)


class Genre(models.Model):
    name = models.CharField(max_length=100, help_text="Genre's name")

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=250)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(help_text="summary here", null=True)
    genre = models.ManyToManyField(Genre)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
