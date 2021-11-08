from django import forms
from .models import Article


class AddArticle(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['science'].empty_label = 'Наука не выбрана'

    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'science']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

class EditArticle(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['science'].empty_label = 'Наука не выбрана'

    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'science']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }