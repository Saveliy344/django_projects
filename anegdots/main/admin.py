from django import forms
from django.contrib import admin
from .models import Anegdot, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AnegdotAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Anegdot
        fields = '__all__'


class AnegdotAdmin(admin.ModelAdmin):
    form = AnegdotAdminForm
    list_display = ('id',)
    list_display_links = ('id',)
    search_fields = ('id', 'text')
    fields = ('category', 'text')
    save_on_top = True


admin.site.register(Anegdot, AnegdotAdmin)
admin.site.register(Category)

# Register your models here.

admin.site.site_title = 'Управление анекдотами'
admin.site.site_header = 'Управление анекдотами'
