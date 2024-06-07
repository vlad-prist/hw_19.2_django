from django.urls import path
from catalog.views import CategoryListView, CategoryDetailView, ProductDetailView, ContactsTemplateView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('', CategoryListView.as_view(), name='category_main_page'),
    path('catalog/<int:pk>/', CategoryDetailView.as_view(), name='category_one'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products')
]
