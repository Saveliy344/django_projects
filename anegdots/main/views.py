import random
from django.contrib.auth import login, logout
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .mixins import CategoryMixin
from .models import Anegdot, Category
from django.contrib.messages import success, error
from .forms import RegForm, LoginForm, ContactForm
from django.core.mail import send_mail


class Main(CategoryMixin, ListView):
    model = Anegdot
    context_object_name = 'anegdots'
    template_name = 'main/main_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context = super().get_user_context(selected=0, title='Анекдоты', search=self.request.GET.get('search', ''))
        return {**context, **new_context}

    def get_queryset(self):
        if self.request.GET.get('search'):
            return Anegdot.objects.filter(text__icontains=self.request.GET.get('search')).select_related('category')
        return Anegdot.objects.all().select_related('category')


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
        return Anegdot.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class AnegdotView(CategoryMixin, DetailView):
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


def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            success(request, "Вы успешно зарегистрировались!")
            login(request, user)
            return redirect('main')
        else:
            error(request, "Ошибка при регистрации!")
    else:
        form = RegForm()
    context = {}
    context['title'] = 'Регистрация'
    context['form'] = form
    return render(request, 'main/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = LoginForm()
    context = {}
    context['title'] = 'Войти'
    context['form'] = form
    return render(request, 'main/register.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


def send_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'],
                             'email_from',
                             ['email_to'], fail_silently=True)
            if mail:
                success(request, 'Письмо успешно отправлено!')
                return redirect('main')
            else:
                error(request, 'Ошибка отправки письма!')
    else:
        form = ContactForm()
    context = {}
    context['title'] = 'Обратная связь'
    context['form'] = form
    return render(request, 'main/register.html', context)
