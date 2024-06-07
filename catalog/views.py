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


# def category_main_page(request):
#     category = Category.objects.all()
#     context = {
#         'category_list': category,
#         'title': 'Каталог товаров',
#     }
#     return render(request, 'catalog/category_main_page.html', context)


# def category_one(request, pk):
#     category_one = get_object_or_404(Category, pk=pk)
#     prod_cat = category_one.products.all()
#
#     context = {
#         'category_one': category_one,
#         'title': f'{category_one.name}',
#         'prod_cat': prod_cat,
#     }
#     return render(request, 'catalog/category_one.html', context)


# def products(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'products_list': product,
#         'title': f'{product.name}',
#         'description': f'{product.description}',
#         'image': f'{product.image}',
#         'price': f'{product.price}',
#     }
#     return render(request, 'catalog/products.html', context)


# def product_detail(request, pk):
#     product_one = get_object_or_404(Product, pk=pk)
#
#     context = {
#         'product_one': product_one,
#         'title': f'{product_one.name}',
#
#     }
#     return render(request, 'catalog/products.html', context)
