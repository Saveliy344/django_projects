from django import template
from women.models import *
from django.db.models import Count
from django.core.cache import cache
register = template.Library()


@register.simple_tag()
def get_categories(fil=None):
    if not fil:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=fil)


@register.inclusion_tag("women/list_categories.html")
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.annotate(count=Count('get_posts'))
    else:
        cats = Category.objects.order_by(sort).annotate(count=Count('get_posts'))
    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag(takes_context=True, filename="women/list_menu.html")
def show_menu(context, register):
    if register:
        menu = [{'title': 'О сайте', 'url_name': 'about'},
                {'title': 'Добавить страницу', 'url_name': 'addpage'},
                {'title': 'Обратная связь', 'url_name': 'contact'},
                ]
    else:
        menu = [{'title': 'О сайте', 'url_name': 'about'},
                {'title': 'Обратная связь', 'url_name': 'contact'},
                ]
    context["menu"] = menu
    context["register"] = register
    return context
