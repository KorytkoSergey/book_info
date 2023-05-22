import factory
from faker import Factory

from reader import models

factory_ru = Factory.create('ru-RU')

class Reader(factory.django.DjangoModelFactory):
    name = factory_ru.word()
    surname = factory_ru.word()
    date_birth = factory_ru.date_time()
    slug = factory_ru.word()

    class Meta:
        model = models.Reader