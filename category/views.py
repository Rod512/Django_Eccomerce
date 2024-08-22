from django.shortcuts import render
from store.models import Product,ReviewRating


def home(request):
    products = Product.objects.all().filter(is_avilable = True).order_by('created_date')
    #get the review
    for product in products:
        reviews = ReviewRating.objects.filter(product_id= product.id, status = True)
    context = {
        'products' : products,
        'reviews' : reviews
    }
    return render(request, 'category/index.html',context)