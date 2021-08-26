from .models import *
from django.core.cache import cache

class Mixin:
    paginate_by = 6
    def get_user_context(self, **kwargs):
        context = kwargs
        register = self.request.user.is_authenticated
        cache1 = cache.get('cats')
        if not cache1:
            cache1 = cache.set('cats', Category.objects.all(), 60)
        context['cats'] = cache1
        return context
