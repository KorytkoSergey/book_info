from django import forms
from book import models


class BookSearch(forms.Form):
    title = forms.CharField(label='Поиск по названию',
                            required=False,
                            help_text='Поиск по названию книги')
    year_publishing = forms.IntegerField(label='Год публикации',
                                         min_value=0, required=False,
                                         help_text='на-р 1990')
    publishing_house = forms.CharField(label='Издательство',
                                       required=False)
    author = forms.CharField(label='Автор',
                             required=False)

    def clean(self):
        author = self.cleaned_data['author']
        if author.isdigit():
            raise forms.ValidationError('Используй буквы')


class BookCreate(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'
