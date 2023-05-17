from django import forms
from book import models


class BookSearch(forms.Form):
    title = forms.CharField(label='Поиск по названию', required=False, help_text='Поиск по названию книги')
    # year_publishing = forms.IntegerField(label='Год публикации', min_value= 0, required=False)
    #
    # def clean(self):  # тоже самое что и функция выше, но можно сразу несколько условий записать
    #     count = self.cleaned_data['year_publishing']
    #     if count.isdigit() is False:
    #         raise forms.ValidationError('Число не равно 10')
    #     return count