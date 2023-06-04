from django.test import TestCase, Client
from django.urls import reverse


class ReaderTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_reader_list(self):
        response = self.client.get(reverse('reader:reader_list'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        data = {
            'name': 'test',
            'surname': 'test2',
            'date_birth': '1999-11-11',
            'slug': 'testtest'
        }
        response = self.client.post(path=reverse('reader:reader_create'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
