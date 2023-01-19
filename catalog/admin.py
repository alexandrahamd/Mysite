from django.contrib import admin
from catalog.models import Product, Category, Blog


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    search_fields = ('name', 'description',)
    list_filter = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'date_of_creation', 'published', 'views')
    prepopulated_fields = {"slug": ("title",)}

