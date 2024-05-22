from django.urls import path
from pages.views import *

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="about")
]
