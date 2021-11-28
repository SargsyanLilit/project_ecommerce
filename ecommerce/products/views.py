from django.shortcuts import render, HttpResponse
from products.models import Products, Product

# Create your views here.


def home(request):
    return render(request, 'products/home.html')


def women(request):
    products = Product.objects.filter(gender="Women")
    for product in products:
        product.images = product.images.split(' ~')
        print(product.images)

    context = {
        'products_list': products[:3]
        }
    return render(request, 'products/women.html', context=context)

