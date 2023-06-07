from rest_framework import generics
from api import serializers
from book.models import Book, Author


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer


class AuthorDetail(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer