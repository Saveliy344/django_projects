from django import template
from django.db.models import Count
from django.core.cache import cache

from main.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects.all().annotate(count=Count('anegdot'))
        cache.set('categories', categories, 60)
    return Category.objects.all().annotate(count=Count('anegdot'))
