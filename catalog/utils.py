from django.conf import settings
from django.core.cache import cache

from Mysite.catalog.models import Category


def cache_category():
    queryset = Category.object.all()
    if settings.CACHE_ENABLED:
        key = f'Category_all:{Category.object.all()}'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)

        return cache_data
    return queryset
