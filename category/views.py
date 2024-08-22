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



# def home(request):
#     products = Product.objects.all().filter(is_avilable=True).order_by('created_date')
#     product_reviews = {}  # Dictionary to hold product-specific reviews
    
#     for product in products:
#         reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
#         product_reviews[product.id] = reviews  # Store the reviews in the dictionary with product.id as the key

#     context = {
#         'products': products,
#         'product_reviews': product_reviews  # Pass the dictionary to the context
#     }
#     return render(request, 'category/index.html', context)