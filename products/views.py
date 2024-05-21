from django.shortcuts import render
from products.models import Product


# Create your views here.
def product_detail(request):
    obj = Product.objects.all()
    context = {
        # "name":obj.name,
        # "description":obj.description,
        # "price":obj.price,
        # "active":obj.active,
        # "live":obj.live

        "objects": obj
    }
    return render(request, "detail.html", context)
