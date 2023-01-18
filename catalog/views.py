from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from catalog.models import Product


def home(request):
    context = {
        'object_list': Product.objects.all(),
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        product = Product()
        product.name = request.POST.get("name")
        product.description = request.POST.get("description")
        product.category = request.POST.get("category")
        product.price = request.POST.get("price")
        product.save()
    return HttpResponseRedirect("/")
