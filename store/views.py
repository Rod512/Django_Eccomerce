from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category 

def store(request, category_slug=None):
    catogries = None
    products = None
    if category_slug != None:
        catogries = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.all().filter(category = catogries, is_avilable = True)
        product_count = products.count()

    else:
        products = Product.objects.all().filter(is_avilable = True)
        product_count = products.count()

    context = {
        'products' : products,
        'product_count' : product_count
    }
    return render(request,'store/store.html', context)
