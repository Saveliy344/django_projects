import random

from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .mixins import CategoryMixin

from .models import Anegdot, Category


class Main(CategoryMixin, ListView):
    model = Anegdot
    context_object_name = 'anegdots'
    template_name = 'main/main_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = super().get_user_context(selected=0, title='Анекдоты')
        return {**context, **new_context}

    def get_queryset(self):
        return Anegdot.objects.all()


class CategoryList(CategoryMixin, ListView):
    model = Anegdot
    context_object_name = 'anegdots'
    template_name = 'main/main_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = super().get_user_context(selected=Category.objects.get(slug=self.kwargs.get('slug')).pk,
                                               title=Category.objects.get(slug=self.kwargs.get('slug')).name)
        return {**context, **new_context}

    def get_queryset(self, *args, **kwargs):
        return Anegdot.objects.filter(category__slug=self.kwargs.get('slug'))


class AnegdotView(DetailView, CategoryMixin):
    model = Anegdot
    context_object_name = 'anegdot'
    pk_url_kwarg = 'pk'
    template_name = 'main/anegdot.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = super().get_user_context(selected=-1, title='Анекдот №' + str(self.kwargs.get('pk')))
        return {**context, **new_context}


def get_random_anegdot(request, *args, **kwargs):
    random.seed(version=2)
    number = random.randint(0, Anegdot.objects.count() - 1)
    pk = Anegdot.objects.all()[number].pk
    return redirect('anegdot', pk=pk)


class Search(CategoryMixin, ListView):
    template_name = 'main/main_page.html'
    model = Anegdot
    context_object_name = 'anegdots'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = super().get_user_context(selected=-1, title='Анекдоты')
        return {**context, **new_context}

    def get_queryset(self):
        return Anegdot.objects.filter(text__icontains=self.request.GET.get('search'))
