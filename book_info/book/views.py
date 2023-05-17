from book import models, forms
from django.views.generic import DetailView, ListView
from .models import Genre, Author, Book


class TitleMixin:
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()
        return context


class TotalList(TitleMixin, ListView):
    model = models.Book
    template_name = 'book/list.html'
    title = 'Список книг'

    def get_queryset(self):
        title = self.request.GET.get('title')
        qs = models.Book.objects.all()
        if title:
            return qs.filter(title__icontains=title)
        return qs



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.BookSearch(self.request.GET or None)
        list_type = self.kwargs['list_type']
        context['class_name'] = list_type

        if list_type == 'book_list':
            book_list = Book.objects.all()
            context['book_list'] = book_list
        elif list_type == 'author_list':
            author_list = Author.objects.all()
            context['author_list'] = author_list
        elif list_type == 'genre_list':
            genre_list = Genre.objects.all()
            context['genre_list'] = genre_list
        return context


class InfoCard(TitleMixin, DetailView):
    template_name = 'book/info_card.html'
    slug_url_kwarg = 'slug'

    def get_model(self):
        list_type = self.kwargs['list_type']
        if list_type == 'author':
            return models.Author
        else:
            return models.Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_type = self.kwargs['list_type']
        context['class_name'] = list_type

        if list_type == 'author':
            author = self.get_object()
            context['book_list'] = author.author_book.all()
            genre_list = set(Genre.objects.filter(genre_book__author_id=author))
            context['genre_list'] = genre_list
        elif list_type == 'book':
            book = self.get_object()
            context['genre_list'] = book.genre_id.all()

        return context

    def get_queryset(self):
        model = self.get_model()
        queryset = model._default_manager.all()
        return queryset




class BookList(TitleMixin, ListView):
    model = models.Book
    template_name = 'book/book_list.html'
    title = 'Список книг'

    def get_queryset(self):
        title = self.request.GET.get('title')
        qs = models.Book.objects.all()
        if title:
            return qs.filter(title__icontains=title)
        print("Title:", title)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.BookSearch(self.request.GET or None)
        print(context)
        return context
