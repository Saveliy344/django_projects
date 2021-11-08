from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.
class ScientistsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_html_photo', 'time_create', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('is_published', )
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50px>")

    get_html_photo.short_description = 'Фотокарточка'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'time_create', 'text')
    search_fields = ('text', 'email', 'name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Scientists, ScientistsAdmin)
admin.site.register(Feedback, FeedbackAdmin)
