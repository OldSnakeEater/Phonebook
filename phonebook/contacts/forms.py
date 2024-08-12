from django import forms
from .models import Contact


class AddContactForm(forms.Form):
    name = forms.CharField(label='', max_length=100, required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Ф.И.О.', 'class': 'modalInput'}))
    subdivision = forms.CharField(label='', max_length=100, required=False,
                                  widget=forms.TextInput(attrs={'placeholder': 'Отдел', 'class': 'modalInput'}))
    number = forms.CharField(label='', max_length=100,  required=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Номер', 'class': 'modalInput'}))
    jobtitle = forms.CharField(label='', max_length=100,  required=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Должность', 'class': 'modalInput'}))
    email = forms.EmailField(label='', max_length=100,  required=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'modalInput'}))
    image = forms.ImageField(label='',  required=False,
                             widget=forms.FileInput(attrs={'placeholder': 'Фото', 'class': 'modalImgInput'}))

    class Media:
        css = {'all': 'contacts/phonebook.css'}
        js = {'all': 'contacts/phonebook.js'}


class SearchContactForm(forms.Form):
    searchName = forms.CharField(label='', max_length=100, required=False,
                                   widget=forms.TextInput(attrs={'placeholder': 'Ф.И.О.', 'class': 'mainInput'}))
    searchNumber = forms.CharField(label='', max_length=100, required=False,
                                   widget=forms.TextInput(attrs={'placeholder': 'Номер', 'class': 'mainInput'}))
    searchSubdivision = forms.CharField(label='', max_length=100, required=False,
                                   widget=forms.TextInput(attrs={'placeholder': 'Отдел', 'class': 'mainInput'}))
    searchJobTitle = forms.CharField(label='', max_length=100, required=False,
                                   widget=forms.TextInput(attrs={'placeholder': 'Должность', 'class': 'mainInput'}))
    searchEmail = forms.CharField(label='', max_length=100, required=False,
                                   widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'mainInput'}))


class ChangeContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'subdivision', 'jobtitle', 'number', 'mail', 'photo']
        labels = {'name': 'Ф.И.О. ', 'subdivision': 'Отдел ', 'jobtitle': 'Должность ', 'number': 'Номер ',
                                                    'mail': 'Почта ', 'photo': 'Фото'}
