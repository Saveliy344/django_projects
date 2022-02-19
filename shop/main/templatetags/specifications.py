from main.models import *
from django import template

register = template.Library()
SPEC = {SmartPhone: ({'diagonal': 'Диагональ'}, {'colour': 'Цвет'},
                     {'capacity': 'Ёмкость батареи'},
                     {'camera': 'Камера'},
                     {'processor': 'Процессор'},
                     {'ram': 'ОЗУ'},
                     {'cores': 'Число ядер'},
                     {'memory': 'Размер встроенной памяти'},
                     {'resolution': 'Разрешение'}),
        Chainsaw: ({'length': 'Длина'}, {'capacity': 'Ёмкость аккумулятора'}, {'power': 'Мощность'}),
        Axe: ({'length': 'Длина, см'}, {'weight': 'Вес, кг'})}


@register.inclusion_tag(filename='main/get_specifications.html')
def get_specifications(product):
    type = product.category.content_type.model_class()
    special_product = type.objects.get(slug=product.slug)  # Продукт в конкретной модели (например, смартфон)
    all_specifications = SPEC.get(type)
    if not all_specifications:
        pass
    current_values = {}
    for spec in all_specifications:
        for key, value in spec.items():
            current_values[value] = getattr(special_product, key)
    return {'specifications': current_values}
