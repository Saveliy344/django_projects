from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_photo_html', 'is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('id', 'title', 'time_create')
    list_filter = ('time_create', 'is_published')
    prepopulated_fields = {"slug": ('title',)}
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'is_published', 'time_create', 'time_update', 'get_photo_html')
    readonly_fields = ('time_create', 'time_update', 'get_photo_html')
    save_on_top = True
    def get_photo_html(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50px height=50px>")
        else:
            return 'Нет фото'
    get_photo_html.short_description = 'Фотокарточка в досье'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_title = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.

admin.site.site_title = 'Администрирование сайта о женщинах'
admin.site.site_header = 'Администрирование сайта о женщинах'
