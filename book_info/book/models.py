from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField('Имя', max_length=255)
    surname = models.CharField('Фамилия', max_length=255)
    date_birth = models.DateField('Дата рождения', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return (self.name + ' ' + self.surname)


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField('Жанр', max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_book')
    genre_id = models.ManyToManyField(Genre, related_name='genre_book')
    publishing_house = models.CharField('Издательство', max_length=255)
    year_publishing = models.IntegerField('Год издания', blank=True, null=True)
    reader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reader_book', blank=True, null=True)

    def __str__(self):
        return self.title
