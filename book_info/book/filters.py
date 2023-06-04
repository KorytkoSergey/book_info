import django_filters as filters

from book import models


class BookFilter(filters.FilterSet):
    class Meta:
        model = models.Book
        fields = ['title', 'author_id', 'year_publishing', 'genre_id', ]
