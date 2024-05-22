from django.urls import path

from .views import *

urlpatterns = [
    path("", product_detail, name="product detail")
]
