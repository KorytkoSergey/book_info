from book import models, forms, filters
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
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


class SearchBook(TitleMixin, ListView):
    model = models.Book
    template_name = 'book/search_book.html'
    title = 'Список книг'
    def get_filters(self):
        return filters.BookFilter(self.request.GET)

    def get_queryset(self):
        # title = self.request.GET.get('title')
        # year_publishing = self.request.GET.get('year_publishing')
        # publishing_house = self.request.GET.get('publishing_house')
        # author = self.request.GET.get('author')
        # qs = models.Book.objects.all()
        # filter_q = Q()
        # if title or year_publishing or publishing_house or author:
        #     if title:
        #         filter_q |= Q(title__icontains=title)
        #     if year_publishing:
        #         filter_q |= Q(year_publishing=year_publishing)
        #     if publishing_house:
        #         filter_q |= Q(publishing_house__icontains=publishing_house)
        #     if author:
        #         author_parts = author.split()
        #         for part in author_parts:
        #             filter_q |= Q(author_id__name__icontains=part)
        #             filter_q |= Q(author_id__surname__icontains=part)
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filters()
        return context


class SearchAuthor(TitleMixin, ListView):
    model = models.Author
    template_name = 'book/search_author.html'
    title = 'Список авторов'

    def get_queryset(self):
        title = self.request.GET.get('title')
        qs = models.Author.objects.all()
        if title:
            return qs.filter(title__icontains=title)
        print("Title:", title)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.BookSearch(self.request.GET or None)
        print(context)
        return context


class SearchGenre(TitleMixin, ListView):
    model = models.Genre
    template_name = 'book/search_genre.html'
    title = 'Список жанров'

    def get_queryset(self):
        title = self.request.GET.get('title')
        qs = models.Genre.objects.all()
        if title:
            return qs.filter(title__icontains=title)
        print("Title:", title)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.BookSearch(self.request.GET or None)
        print(context)
        return context

class BookCreate(TitleMixin, CreateView):
    model = models.Book
    template_name = 'book/book_create.html'
    form_class = forms.BookCreate
    success_url = reverse_lazy('book:book_list')

