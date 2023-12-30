from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class SignUp(UserCreationForm):
    username = forms.CharField(label='логин',
                               help_text='',
                               widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password1 = forms.CharField(label='пароль',
                                help_text='', widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password"}
        )
                                )
    password2 = forms.CharField(label='подтверждение',
                                help_text='', widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password"}
        )
                                )
    email = forms.EmailField(label='почта',
                             widget=forms.TextInput(attrs={'placeholder': 'qwe@mail.ru'})
                             )
    first_name = forms.CharField(label='имя', max_length=20, required=False)
    last_name = forms.CharField(label='фамилия', max_length=20, required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
