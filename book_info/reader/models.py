from django.db import models


class Reader(models.Model):
    name = models.CharField('Имя', max_length=255)
    surname = models.CharField('Фамилия', max_length=255)
    date_birth = models.DateField('Дата рождения', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return (self.name + ' ' + self.surname)
