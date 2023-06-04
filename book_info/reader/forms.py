from django import forms
from reader import models


class ReaderSearch(forms.Form):
    name = forms.CharField(label='Имя', required=False)
    surname = forms.CharField(label='Фамилия', required=False)
    date_birth = forms.DateField(label='Дата рождения', required=False)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        surname = cleaned_data.get('surname')

        if name.isdigit() or surname.isdigit():
            raise forms.ValidationError('Используй буквы')

        return cleaned_data


class ReaderCreate(forms.ModelForm):
    class Meta:
        model = models.Reader
        fields = '__all__'
