from django.shortcuts import render


# Create your views here.
def home(request):
    list = ["js", "py", "php", "c#", "c++", "ruby"]
    context = {
        "list":list
    }
    user = request.user

    if user.is_authenticated:
        context = {
            "list" : list,
            "user": user

        }
    if user.is_authenticated:
        context['user'] = user

    else:
        context["user"] = "deconnecté"
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")

