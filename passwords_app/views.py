from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "pages/home.html")

def generate(request):
    return render(request, "pages/generate.html")


def password(request):

    basic_characters = list("abcdefghijklmnopqrstuvwxyz")
    generate_password = ""

    ### Leer lo que viene a través de la query
    lenght = int(request.GET.get("lenght"))

    uppercase = request.GET.get("uppercase")

    special = request.GET.get("special")

    numbers = request.GET.get("numbers")

    return render(request, "pages/password.html")