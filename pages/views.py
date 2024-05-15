from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<h1>Home</h1>")


def about(request):
    return HttpResponse("About page")


def contact(request):
    print(request.user)
    return HttpResponse("Contacts page")