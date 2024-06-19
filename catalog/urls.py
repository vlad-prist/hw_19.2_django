from django.urls import path
from catalog.views import (CategoryListView, CategoryDetailView, ProductDetailView, ContactsTemplateView,
                           ProductCreateView, ProductUpdateView, ProductDeleteView)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('', CategoryListView.as_view(), name='categories_list'),
    path('catalog/<int:pk>/', CategoryDetailView.as_view(), name='category_one'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
]
