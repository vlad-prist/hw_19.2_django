from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (
    CategoryListView,
    CategoryDetailView,
    ProductDetailView,
    ContactsTemplateView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("", CategoryListView.as_view(), name="categories_list"),
    path("catalog/<int:pk>/", CategoryDetailView.as_view(), name="category_one"),
    path(
        "products/<int:pk>/",
        cache_page(60 * 60)(ProductDetailView.as_view()),
        name="products",
    ), # Кеширование на 1 час
    path("create/", ProductCreateView.as_view(), name="create"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="delete"),
]
