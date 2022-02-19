from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView
from .forms import FBForm, CommentForm, OrderForm, UserRegistration
from django.core.mail import send_mail
from .models import Product, Category, Comment, Customer, CartProduct, Cart, Order


class Main(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'main/base.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Главная'
        return context


class Categories(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'main/base.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category = Category.objects.get(slug=self.kwargs.get('slug'))
        context['title'] = category.name
        return context

    def get_queryset(self, *args, **kwargs):
        return Product.objects.filter(category__slug=self.kwargs.get('slug'))


def get_product(request, *args, **kwargs):
    context = {'product': Product.objects.get(slug=kwargs.get('slug')),
               'comments': Comment.objects.filter(product__slug=kwargs.get('slug'))}
    if request.method == 'POST':
        if 'message' in request.POST:
            if not request.user.is_authenticated:
                return redirect('login')
            comment = CommentForm(request.POST)
            if comment.is_valid():
                Comment.objects.create(product=context['product'], customer=Customer.objects.get(user=request.user),
                                       content=comment.cleaned_data['message'])
                return redirect(reverse('product', kwargs={'slug': kwargs.get('slug')}))
        else:
            if not request.user.is_authenticated:
                return redirect('main')
            cart = Cart.objects.filter(customer__user=request.user, on_order=False).last()
            if not cart:
                cart = Cart.objects.create(customer=Customer.objects.get(user=request.user), on_order=False)
            flag = False  # наличие товара в корзине
            for cart_product in cart.products.all():
                if cart_product.product == context['product']:
                    cart_product.value += 1
                    cart_product.cost += cart_product.product.price
                    cart_product.save()
                    cart.cost += cart_product.product.price
                    cart.save()
                    flag = True
                    break
            if flag == False:
                cart_product = CartProduct.objects.create(product=context['product'], value=1,
                                                          cost=context['product'].price)
                cart.products.add(cart_product)
                cart.cost += cart_product.product.price
                cart.save()
            return redirect(reverse('product', kwargs={'slug': kwargs.get('slug')}))
    else:
        comment = CommentForm()
    context['form'] = comment
    context['title'] = context['product'].name
    return render(request, 'main/product.html', context)


def feedback(request):
    if request.method == 'POST':
        form = FBForm(request.POST)
        if form.is_valid():
            send_mail(form.cleaned_data['subject'] + ' от ' + form.cleaned_data['sender'],
                      form.cleaned_data['message'],
                      '***',
                      ['***', '***'], fail_silently=True)
            return redirect('main')
    else:
        form = FBForm()
    context = {'form': form, 'title': 'Обратная связь'}
    return render(request, 'main/feedback.html', context)


def find_sum(queryset):
    sum = 0
    for example in queryset:
        sum += example.cost
    return sum


def get_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    cart = Cart.objects.filter(customer__user=request.user, on_order=False).last()
    if not cart:
        cart = Cart.objects.create(customer=Customer.objects.get(user=request.user), on_order=False)
    context = {'title': 'Корзина', 'cart': cart}
    if request.method == 'POST':
        for product in context['cart'].products.all():
            if product.product.slug in request.POST:
                value = int(request.POST.get(product.product.slug))
                if value <= 0:
                    product.delete()
                else:
                    product.value = value
                    product.cost = product.product.price * value
                    product.save()
        context['cart'].cost = find_sum(context['cart'].products.all())
        context['cart'].save()
        return redirect('cart')
    else:
        return render(request, 'main/cart.html', context)


class SearchView(TemplateView):
    template_name = 'main/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Поиск'
        context['products'] = Product.objects.filter(name__icontains=self.request.GET.get('search'))
        return context


def make_logout(request):
    logout(request)
    return redirect('main')


def make_order(request):
    if not request.user.is_authenticated:
        return redirect('main')
    cart = Cart.objects.filter(customer__user=request.user, on_order=False).last()
    if not cart:
        return redirect('main')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(cart=cart, time_delivery=request.POST.get('time_delivery'),
                                 address=request.POST.get('address'))
            cart.on_order = True
            cart.save()
            return redirect('main')
    else:
        form = OrderForm()
    context = {'title': 'Оформление заказа', 'cart': cart, 'form': form}
    return render(request, 'main/order.html', context)


class RegisterUser(CreateView):
    form_class = UserRegistration
    success_url = reverse_lazy('main')
    template_name = 'main/register.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Регистрация'
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        Customer.objects.create(user=self.request.user)
        return redirect('main')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('main')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Авторизация'
        return context
