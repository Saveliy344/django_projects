from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена, руб')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Фотография')
    slug = models.SlugField(verbose_name='Slug')
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)
    time_update = models.DateTimeField(auto_now=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(verbose_name='Slug категории')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories', kwargs={'slug': self.slug})


class CartProduct(models.Model):
    product = models.ForeignKey('Product', verbose_name='Продукт', on_delete=models.CASCADE)
    value = models.PositiveIntegerField(verbose_name='Количество', default=1)
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость, руб')

    def __str__(self):
        return f"CartProduct:{str(self.product)}"


class Cart(models.Model):
    products = models.ManyToManyField('CartProduct', verbose_name='Продукты', related_name='Products', blank=True)
    customer = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость корзины, руб', default=0)
    on_order = models.BooleanField()

    def __str__(self):
        return f'Корзина №{self.pk}'


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Фотография профиля')

    def __str__(self):
        return f'Покупатель {self.user.username}'


class SmartPhone(Product):
    diagonal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Диагональ, дюймы')
    colour = models.CharField(max_length=255, verbose_name='Цвет')
    capacity = models.PositiveIntegerField(verbose_name='Ёмкость, мАч')
    camera = models.PositiveIntegerField(verbose_name='Камера, Мпикс')
    processor = models.CharField(max_length=255, verbose_name='Процессор')
    ram = models.PositiveIntegerField(verbose_name='ОЗУ, Гб')
    cores = models.PositiveIntegerField(verbose_name='Число ядер процессора')
    memory = models.PositiveIntegerField(verbose_name='Встроенная память, Гб')
    resolution = models.CharField(verbose_name='Разрешение экрана', max_length=255)


class Chainsaw(Product):
    length = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Длина шины, см')
    capacity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Объём двигателя, см^3')
    power = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Мощность, л.с.')


class Comment(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Покупатель')
    content = models.CharField(max_length=528, verbose_name='Комментарий')
    time_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    time_updated = models.DateTimeField(verbose_name='Дата последнего обновления', auto_now=True)

    def __str__(self):
        return f"Комменатрий от {self.customer.user.username} {self.time_created}"

    class Meta:
        ordering = ['-time_updated', ]


class Order(models.Model):
    time_delivery = models.DateField(verbose_name='Дата доставки')
    address = models.CharField(max_length=250, verbose_name='Адрес доставки')
    cart = models.OneToOneField(Cart, verbose_name='Заказ', on_delete=models.CASCADE)


class Axe(Product):
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вес, кг')
    length = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Длина, см')
