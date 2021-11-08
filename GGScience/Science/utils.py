from .models import *


class Mixin:
    paginate_by = 6
    def get_user_context(self, **kwargs):
        context = kwargs
        register = self.request.user.is_authenticated
        sciences = Science.objects.all()
        context['sciences'] = sciences
        return context
