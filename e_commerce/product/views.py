from django.shortcuts import render, get_object_or_404
from .models import Product, ProductSpecification

# Create your views here.
def home(request):
    context = {}
    return render(request, 'product/home.html', context)


def all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/all_products.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    product_specifications =ProductSpecification.objects.select_related('specification').filter(product=product)
    context = {'product': product, 'product_specifications': product_specifications}
    return render(request, 'product/product_detail.html', context)