from django.urls import path

from .views import *

urlpatterns = [
    path("product_detail/", product_detail, name="product detail"),
    path("product_create/", product_create, name="product_create"),
    # path("product_create_view/", product_create_view, name="product_create"),
]
