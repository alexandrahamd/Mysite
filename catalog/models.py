from datetime import datetime
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(default='', max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.CharField(max_length=250, blank=True, null=True)
    preview = models.ImageField(max_length=200, blank=True, null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    views = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.title


