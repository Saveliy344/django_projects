from .models import *
from django.core.cache import cache

class Mixin:
    paginate_by = 6
    def get_user_context(self, **kwargs):
        context = kwargs
        register = self.request.user.is_authenticated
        cats = Category.objects.all()
        context['cats'] = cats
        return context
