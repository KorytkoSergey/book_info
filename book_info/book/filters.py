import django_filters as filters

from book import models


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year', 'isbn', 'quantity']