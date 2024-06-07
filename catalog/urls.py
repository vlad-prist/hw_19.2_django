from django.urls import path
from catalog.views import contacts, CategoryListView, CategoryDetailView, ProductDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', CategoryListView.as_view(), name='category_main_page'),
    path('catalog/<int:pk>/', CategoryDetailView.as_view(), name='category_one'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products')
]
