from rest_framework import generics
from api import serializers
from book.models import Book


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer


class AuthorDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.AuthorSerializer