from django import template
from main.models import Category
from django.db.models import Count

register = template.Library()


@register.simple_tag()
def categories():
    cats = Category.objects.all().annotate(amount=Count('product'))
    return cats
