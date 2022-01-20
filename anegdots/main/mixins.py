from django.contrib.auth.mixins import LoginRequiredMixin


class CategoryMixin(LoginRequiredMixin):
    paginate_by = 5
    login_url = 'login'

    def get_user_context(self, *, object_list=None, **kwargs):
        new_context = kwargs
        return new_context
