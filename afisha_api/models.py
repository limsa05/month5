from django.db import models


class Cinema(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):

    title = models.CharField(max_length=30)
    description = models.TextField()
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)

class Review(models.Model):
    DoesNotExist = None
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)