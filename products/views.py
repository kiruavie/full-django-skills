from django.shortcuts import render
from .models import Product
from .forms import ProductForm

def product_detail(request):
    obj = Product.objects.all()
    context = {
        "objects": obj
    }
    return render(request, "detail.html", context)

def product_create(request):
    form = ProductForm(request.POST or None)
    message = ""
    if form.is_valid():
        form.save()
        message = "Product registered successfully"
        form = ProductForm()
    context = {
        "form": form,
        "message": message
    }
    return render(request, "create.html", context)


# def product_create_view(request):
#     print(request.GET)
#     print(request.POST)

#     return render(request, "create.html")