import factory
from faker import Factory

from book import models

factory_ru = Factory.create('ru-RU')
factory_en = Factory.create('en_US')


class Author(factory.django.DjangoModelFactory):
    author_id = factory_ru.random_int()
    name = factory_ru.word()
    surname = factory_ru.word()
    date_birth = factory_ru.date()
    slug = factory_en.word()

    class Meta:
        model = models.Author


class Genre(factory.django.DjangoModelFactory):
    genre_id = factory_ru.random_int()
    name = factory_ru.word()

    class Meta:
        model = models.Genre


class Book(factory.django.DjangoModelFactory):
    book_id = factory_ru.random_int()
    author_id = factory.SubFactory(Author)
    title = factory_ru.word()
    slug = factory_en.word()
    publishing_house = factory_ru.word()
    year_publishing = factory_ru.random_digit_not_null()

    class Meta:
        model = models.Book

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for genre in extracted:
                self.genre_id.add(genre)
