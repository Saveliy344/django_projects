from django.db import models
from django.urls import reverse


class Anegdot(models.Model):
    text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"Анекдот #{self.pk}"


class Category(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=69)

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
