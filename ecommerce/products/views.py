from django.shortcuts import render, HttpResponse, redirect
from products.models import Products, Product
from products.forms import ProductQuantityForm

# Create your views here.


def home(request):
    return render(request, 'products/home.html')


def women(request):
    products = Product.objects.filter(gender="Women")
    for product in products:
        product.images = product.images.split(' ~')

    context = {
        'products_list': products[:3]
        }
    return render(request, 'products/women.html', context=context)


def product_view(request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            product.images = product.images.split(' ~')
        except Product.DoesNotExist:
            return redirect('home')

        product_form = ProductQuantityForm(instance=product)

        return render(request, "products/product_view.html", context={'product': product, 'form': product_form})

