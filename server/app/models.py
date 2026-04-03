from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=256)
    year = models.CharField(max_length=4, null=True)
    imdb_title_id = models.CharField(max_length=20, unique=True)


class MovieQueryHistory(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
