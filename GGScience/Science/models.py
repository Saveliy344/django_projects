from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Статья")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    science = models.ManyToManyField('Science', verbose_name='Наука')

    class Meta:
        verbose_name = 'Научная статья'
        verbose_name_plural = 'Научные статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_article', kwargs={'slug_name': self.slug})

class Science(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название науки")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Наука'
        verbose_name_plural = 'Науки'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_science', kwargs={'slug_name': self.slug})