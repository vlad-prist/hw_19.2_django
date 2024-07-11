from django.core.cache import cache

from config.settings import CACHE_ENABLED
from catalog.models import Category


def get_category_list_from_cache():
    """ Получает данные по категориям из кеша, если кеш пуст, то данные берутся из БД """
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = 'category_list'
    category_list = cache.get(key)
    if category_list is not None:
        return category_list
    category_list = Category.objects.all()  # Берем данные из БД
    cache.set(key, category_list, 60 * 60) # Кеширование на 1 час
    return category_list

