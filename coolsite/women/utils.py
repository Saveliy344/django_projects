from .models import *
from django.db.models import Count
class DataMixin:
    paginate_by = 5
    def get_user_context(self, **kwargs):
        context = kwargs
        if 'cat_selected' not in kwargs:
            context['cat_selected'] = 0
        context['register'] = False
        if self.request.user.is_authenticated:
            context['register'] = True
        return context