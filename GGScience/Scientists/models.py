from django.db import models
from django.urls import reverse


class Feedback(models.Model):
    email = models.EmailField(max_length=255, verbose_name="Почта")
    name = models.CharField(max_length=255, verbose_name="Имя")
    text = models.TextField(verbose_name="Доклад")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время доклада")

    class Meta:
        verbose_name = 'Доклад'
        verbose_name_plural = 'Доклады'


class Scientists(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to="%photos/%Y/%m/%d", verbose_name="Фотокарточка в досье")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Создание")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория", related_name='get_posts')

    class Meta:
        verbose_name = 'Учёный'
        verbose_name_plural = 'Ученые'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('showpost', kwargs={'slug_name': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug_name': self.slug})
