from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField

class RegForm(UserCreationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    email = forms.CharField(max_length=150, label='Email',
                            widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=150, label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=150, label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password = forms.CharField(max_length=150, label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=150, label='Субъект',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    content = forms.CharField(max_length=150, label='Содержимое',
                              widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5, 'autocomplete': 'off'}))
    captcha = CaptchaField()