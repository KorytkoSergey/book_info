from django.test import TestCase, Client
from django.urls import reverse
from book import models
class BookTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_book_list(self):
        response = self.client.get(reverse('book:search_book'))
        self.assertEqual(response.status_code, 200)

class AuthorTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.author = models.Author.objects.create(name='Лосяш', surname='Бараш', date_birth='1976-09-11', slug='lb')

    def test_detail(self):
        response = self.client.get(reverse('book:author', kwargs={'slug':self.author.slug}))
        self.assertEqual(response.status_code, 200)