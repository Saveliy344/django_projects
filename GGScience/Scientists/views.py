from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, DeleteView

from .forms import AddPostForm, UpdatePostForm, RegisterUserForm, LoginUserForm, FeedBackForm
from .models import *
from .utils import Mixin


class Home(Mixin, ListView):
    model = Scientists
    context_object_name = 'posts'
    template_name = 'Scientists/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = self.get_user_context(**kwargs, title='Главная страница', selected=0)
        return {**context, **new_context}

    def get_queryset(self):
        return Scientists.objects.filter(is_published=True).select_related('cat')


class ShowCategory(Mixin, ListView):
    model = Scientists
    context_object_name = 'posts'
    template_name = 'Scientists/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.get(slug=self.kwargs['slug_name'])
        new_context = self.get_user_context(**kwargs, title=cat.name, selected=cat.id)
        return {**context, **new_context}

    def get_queryset(self):
        return Scientists.objects.filter(cat__slug=self.kwargs['slug_name'], is_published=True).select_related('cat')


class Addpage(LoginRequiredMixin, Mixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = AddPostForm
    success_url = reverse_lazy('home')
    template_name = 'Scientists/AddPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_context = self.get_user_context(title='Добавить страницу', selected=-1)
        return {**context, **common_context}


def about(request):
    return render(request, 'Scientists/about.html',
                  {'cats': Category.objects.all(), 'selected': -1, 'title': 'Про нас'})


def contact(request):
    return HttpResponse("")


class ShowPost(Mixin, DetailView):
    model = Scientists
    slug_url_kwarg = 'slug_name'
    context_object_name = 'post'
    template_name = 'Scientists/show_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'].title, selected=context['post'].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    if not request.user.is_authenticated:
        return redirect('home')
    logout(request)
    return redirect('login')


class UpdatePost(LoginRequiredMixin, Mixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Scientists
    context_object_name = 'post'
    slug_url_kwarg = 'slug_name'
    form_class = AddPostForm
    template_name = 'Scientists/Updater.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = self.get_user_context(title='Обновление поста', selected=context['post'].cat_id)
        return {**context, **new_context}

    def get_success_url(self):
        return reverse_lazy('home')


class DeletePost(LoginRequiredMixin, Mixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'Scientists/delete_post.html'
    context_object_name = 'post'
    model = Scientists
    slug_url_kwarg = 'slug_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = self.get_user_context(title='Удаление поста', selected=context['post'].cat_id)
        return {**context, **new_context}

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(Mixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'Scientists/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = self.get_user_context(title='Главная страница')
        return {**context, **new_context}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(Mixin, LoginView):
    form_class = LoginUserForm
    template_name = 'Scientists/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = self.get_user_context(title='Вход')
        return {**context, **new_context}

    def get_success_url(self):
        return reverse_lazy('home')


class FeedBack(Mixin, CreateView):
    form_class = FeedBackForm
    template_name = 'Scientists/feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = self.get_user_context(title='Обратная связь')
        return {**context, **new_context}

    def get_success_url(self):
        return reverse_lazy('home')
