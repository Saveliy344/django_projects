from .models import Category
from django.db.models import Count


class CategoryMixin:
    paginate_by = 2

    def get_user_context(self, *, object_list=None, **kwargs):
        new_context = kwargs
        new_context['categories'] = Category.objects.all().annotate(count=Count('anegdot'))
        return new_context
