from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import CartProduct, Order


class FBForm(forms.Form):
    subject = forms.CharField(label='Тема письма',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
                              max_length=100)
    message = forms.CharField(label='Текст письма',
                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'autocomplete': 'off'}))
    sender = forms.EmailField(label='E-mail отправителя',
                              widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))


class CommentForm(forms.Form):
    message = forms.CharField(label='Комментарий',
                              widget=forms.Textarea(attrs={'class': 'form-control', 'autocomplete': 'off', 'rows': 4}),
                              max_length=150)


class CartProductForm(forms.ModelForm):
    class Meta:
        model = CartProduct
        fields = ['value', ]
        widgets = {
            'value': forms.TextInput(attrs={'type': 'number', 'class': 'form-control', 'autocomplete': 'off'})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['time_delivery', 'address']
        widgets = {
            'time_delivery': forms.TextInput(attrs={'type': 'date'}),
            'address': forms.TextInput(attrs={'type': 'address'}),
        }


class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
