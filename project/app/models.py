from django.db import models


class Author(models.Model):
    name = models.CharField()

class Genre(models.Model):
    type = models.CharField()

class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books_author')
    genre = models.ManyToManyField(Genre,  related_name='books_genre', blank=True)



