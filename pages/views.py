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
    list = [1,2,3,4,3,7,8,0,6]
    context = {
        "list":list,
        "title": "about us",
        "number":123
    }
    return render(request, "about.html", context)




def contact(request):
    return render(request, "contact.html")

