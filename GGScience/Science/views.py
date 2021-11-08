from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView, DetailView, DeleteView
from .utils import Mixin
from .models import *
from .forms import AddArticle, EditArticle


class Science_articles(Mixin, ListView):
    model = Article
    context_object_name = 'posts'
    template_name = 'Science/show_articles.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = self.get_user_context(title='Научные статьи', selected=0)
        return {**new_context, **context}

    def get_queryset(self):
        return Article.objects.all().prefetch_related('science')


class ShowCategory(Mixin, ListView):
    model = Article
    context_object_name = 'posts'
    template_name = 'Science/show_articles.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = self.get_user_context(title=Science.objects.get(slug=self.kwargs['slug_name']),
                                            selected=Science.objects.get(slug=self.kwargs['slug_name']).pk)
        return {**new_context, **context}

    def get_queryset(self):
        return Article.objects.filter(science__slug=self.kwargs['slug_name']).prefetch_related('science')


class AddArticle(Mixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = AddArticle
    success_url = reverse_lazy('science')
    template_name = 'Science/AddArticle.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = self.get_user_context(title='Добавить статью', selected=0)
        return {**new_context, **context}

    def get_success_url(self):
        return reverse_lazy('science')


class EditArticle(Mixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Article
    context_object_name = 'post'
    slug_url_kwarg = 'slug_name'
    form_class = EditArticle
    template_name = 'Science/EditArticle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = self.get_user_context(selected=0, title='Обновить статью')
        return {**new_context, **context}

    def get_success_url(self):
        return reverse_lazy('science')


class ShowArt(Mixin, LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('science')
    model = Article
    slug_url_kwarg = 'slug_name'
    context_object_name = 'post'
    template_name = 'Science/show_article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = self.get_user_context(selected=0, title=Article.objects.get(slug=self.kwargs['slug_name']).title)
        return {**new_context, **context}

    def get_queryset(self):
        return Article.objects.filter(slug=self.kwargs['slug_name'])


class DelArt(Mixin, LoginRequiredMixin, DeleteView):
    slug_url_kwarg = 'slug_name'
    model = Article
    context_object_name = 'post'
    template_name = 'Science/del_art.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = self.get_user_context(selected=0, title='Удалить статью')
        return {**context, **new_context}

    def get_success_url(self):
        return reverse_lazy('science')
