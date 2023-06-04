from django.test import TestCase, Client
from django.urls import reverse
from book import factories


class BookTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.book = factories.Book()

    def test_book_list(self):
        response = self.client.get(reverse('book:search_book'))
        self.assertEqual(response.status_code, 200)


class AuthorTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.author = factories.Author()

    def test_detail(self):
        response = self.client.get(
            reverse('book:author',
                    kwargs={'slug': self.author.slug}))
        self.assertEqual(response.status_code, 200)


class GenreTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.genre = factories.Genre()

    def test_detail(self):
        response = self.client.get(reverse('book:genre_list'))
        self.assertEqual(response.status_code, 200)
