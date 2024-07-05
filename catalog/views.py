from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from catalog.models import Category, Product, Version
from django.urls import reverse_lazy, reverse
from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from django.forms import inlineformset_factory


class ContactsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category

    def get_success_url(self):
        return reverse('catalog:category_one', args=[self.kwargs.get('pk')])


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_success_url(self):
        return reverse('catalog:category_one', args=[self.kwargs.get('pk')])


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:categories_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    #form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:category_one', args=[self.get_object().category.pk]) # kwargs={'pk': self.object.pk}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        permission_required = ['catalog.can_edit_description',
                               'catalog.can_cancel_publishing',
                               'catalog.can_change_category',]
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif [user.has_perm(i for i in permission_required)]:
        # elif user.has_perm('catalog.can_edit_description') and user.has_perm('catalog.can_cancel_publishing') and user.has_perm('catalog.can_change_category'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:categories_list')
