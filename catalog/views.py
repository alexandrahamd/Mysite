from django.db.models import F
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from catalog.models import Blog
from pytils.translit import slugify


def contacts(request):
    return render(request, 'catalog/contacts.html')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return super().get_queryset().filter(views=True)


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
    fields = '__all__'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        article = form.save(commit=False)
        article.slug = slugify(article.title)
        article.save()
        return super().form_valid(form)
