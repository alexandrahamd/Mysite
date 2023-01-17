from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.IntegerField
    date_of_creation = models.DateField
    date_of_change = models.DateField

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name
