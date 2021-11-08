from django.contrib import admin
from .models import *


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}


class ScienceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Science, ScienceAdmin)
