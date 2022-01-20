from django import template

register = template.Library()


@register.simple_tag()
def count_words(string):
    return len(string.split())
