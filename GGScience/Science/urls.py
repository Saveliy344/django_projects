from django.views.decorators.cache import cache_page
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', Science_articles.as_view(), name='science'),
    path('category/<slug:slug_name>/', ShowCategory.as_view(), name='category_science'),
    path('add_article/', AddArticle.as_view(), name='add_article'),
    path('edit_article/<slug:slug_name>/', EditArticle.as_view(), name='edit_article'),
    path('show_article/<slug:slug_name>', ShowArt.as_view(), name='show_article'),
    path('delete_article/<slug:slug_name>/', DelArt.as_view(), name='delete_article'),
]
