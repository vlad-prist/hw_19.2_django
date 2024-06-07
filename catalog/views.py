from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from catalog.models import Category, Product


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f'{name} {phone}\n{message}')
    context = {'title': 'Контакты'}
    return render(request, 'catalog/contacts.html', context)


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category


class ProductDetailView(DetailView):
    model = Product
