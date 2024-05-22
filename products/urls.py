from django.urls import path

from .views import *

urlpatterns = [
    path("product_detail/", product_detail, name="product detail"),
    path("product_create/", product_create, name="product_create")
]
