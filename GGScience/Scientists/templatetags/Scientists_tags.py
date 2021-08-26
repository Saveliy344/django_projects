from django import template
from Scientists.models import *

register = template.Library()


@register.inclusion_tag(takes_context=True, filename="Scientists/menu.html")
def menu(context):
    menu = [{'title': 'О сайте', 'url_name': 'about'},
            {'title': 'Добавить страницу', 'url_name': 'addpage'},
            {'title': 'Обратная связь', 'url_name': 'contact'},
            ]
    context["menu"] = menu
    return context
