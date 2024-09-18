from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from .models import Product, ProductSpecification, Review
from .forms import ReviewForm

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
    product_specifications = ProductSpecification.objects.select_related('specification').filter(product=product)
    product_reviews = Review.objects.filter(product=product, approved=True)
    average_rating = product_reviews.aggregate(Avg('rate'))['rate__avg'] or 0
    context = {
        'product': product, 
        'product_specifications': product_specifications,
        'product_reviews': product_reviews,
        'rating': average_rating
        }
    return render(request, 'product/product_detail.html', context)