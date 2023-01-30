from django.db.models import F
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from catalog.models import Blog, Product, Category, Version
from pytils.translit import slugify
from catalog.forms import ProductForm, VersionForm


def contacts(request):
    return render(request, 'catalog/contacts.html')


class BlogListView(ListView):
    model = Blog

    # def get_queryset(self):
    #     return super().get_queryset().filter(views=True)


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        article = form.save(commit=False)
        article.slug = slugify(article.title)
        article.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    # Добавляем счетчик
    def render_to_response(self, *args, **kwargs):
        self.object.views = F('views') + 1
        self.object.save()
        return super().render_to_response(*args, **kwargs)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content')
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        article = form.save(commit=False)
        article.slug = slugify(article.title)
        article.save()
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateWithVersionView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'catalog/product_with_version.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        FromSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = FromSet(self.request.POST, instance=self.object)
        else:
            formset = FromSet(instance=self.object)

        context_data['formset'] = formset
        return context_data


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')

