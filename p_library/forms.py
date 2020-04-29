from django import forms
from .models import Author, Book, Friend, PublishHouse, UserProfile


my_dict = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Введите страну'
        }


class ProfileCreationForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = []


# Форма автора
class AuthorForm(forms.ModelForm):

    full_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите имя автора'
            }
        )
    )
    birth_year = forms.CharField(
        label='Дата рождения',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите дату рождения'
            }
        )
    )
    country = forms.CharField(
        label='Страна',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите страну'
            }
        )
    )

    class Meta:
        model = Author
        fields = '__all__'


# Форма книги
class BookForm(forms.ModelForm):
    my_dict['placeholder']='Введите любые 13 чисел'
    ISBN = forms.CharField(
        max_length=13,
        label='ISBN',
        widget=forms.TextInput(
            attrs=my_dict
        )
    )
    my_dict['placeholder']='Введите название книги'
    title = forms.CharField(
        label='Название книги',
        widget=forms.TextInput(
            attrs=my_dict
        )
    )
    description = forms.CharField(
        label='Описание книги',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'exampleFormControlTextarea1',
                'rows': '3',
                'placeholder': 'Описание книги'
            }
        )
    )
    year_release = forms.CharField(
        label='Дата публикации',
        widget=forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        label='Автор',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'exampleFormControlSelect1'
            }
        )
    )
    publish_house = forms.ModelChoiceField(
        queryset=PublishHouse.objects.all(),
        label='Издательство',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'exampleFormControlSelect1'
            }
        )
    )
    copy_count = forms.IntegerField(
        label= 'Всего книг',
        widget= forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    price = forms.FloatField(
        label= 'Цена',
        widget= forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    friend = forms.ModelChoiceField(
        required=False,
        queryset=Friend.objects.all(),
        label='У кого находится',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'exampleFormControlSelect1'
            }
        )
    )
    image = forms.ImageField(
        label= 'Фото обложки',
        allow_empty_file=None,
        widget= forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Book
        fields = '__all__'


class FriendForm(forms.ModelForm):
    name_friend = forms.CharField(
        label='Имя друга',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите имя друга'
            }
        )
    )
    class Meta:
        model = Friend
        fields = '__all__'

class BookUpdateForm(forms.ModelForm):
    friend = forms.ModelChoiceField(
        queryset=Friend.objects.all(),
        label='У кого находится',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'exampleFormControlSelect1'
            }
        )
    )
    class Meta:
        
        model = Book
        fields = ['friend']