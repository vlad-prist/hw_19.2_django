# Домашняя работа 21.1

1. В контролере catalog/view.py реализованы классы CBV
- Внесены изменения в урлы;
- в шаблонах изменены переменные на object
- также изменен контроллер Контакты.
- 
Изменения в catalog/view.py:

1.1 вместо
def category_main_page(request):
    category = Category.objects.all()
    context = {'category_list': category, 'title': 'Каталог товаров',}
    return render(request, 'catalog/category_main_page.html', context)

появилось
class CategoryListView(ListView):
    model = Category

1.2 вместо
def category_one(request, pk):
    category_one = get_object_or_404(Category, pk=pk)
    prod_cat = category_one.products.all()
    context = {'category_one': category_one,'title': f'{category_one.name}', 'prod_cat': prod_cat,}
    return render(request, 'catalog/category_one.html', context)

появилось
class CategoryDetailView(DetailView):
    model = Category

1.3 вместо 
def products(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'products_list': product,'title': f'{product.name}','description': f'{product.description}','image': f'{product.image}','price': f'{product.price}',}
    return render(request, 'catalog/products.html', context)

появилось
class ProductDetailView(DetailView):
    model = Product

1.4 метод def product_detail(request, pk) вообще не был использован, также как и шаблон к нему

1.5 вместо
def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f'{name} {phone}\n{message}')
    context = {'title': 'Контакты'}
    return render(request, 'catalog/contacts.html', context)

появилось:
class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context

Данный класс выполнен согласно документации https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.TemplateView

2. Реализовано новое приложение Blog.
К нему создана модель, и контролеры прописаны согласно CRUD

3. В новом приложении реализовано:
-счетчик просмотра
-Выведены статьи у которых признак публикации is_published=True.
Если в классе BlogListView у метода get_queryset изменить фильтр на is_published=False - то выведутся неопубликованные статьи
- сформированы slug для заголовка. 
Создано через переопределение метода form_valid() в CreateView.
- в классе UpdateView после редактирования статьи создано перенаправление на отредактированныую статью через метод def get_success_url(self)