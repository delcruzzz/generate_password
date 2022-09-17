from django.shortcuts import render

import random

# Create your views here.
def home(request):
    return render(request, "pages/home.html")

def generate(request):
    return render(request, "pages/generate.html")


def password(request):

    ### Lógica
    basic_characters = list('abcdefghijklmnopqrstuvwxyz')
    generate_password = ''

    ### Leer lo que viene a través de la query
    lenght =  int(request.GET.get('lenght'))

    uppercase = request.GET.get('uppercase')
    special = request.GET.get('special')
    numbers = request.GET.get('numbers')

    if uppercase:
        basic_characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if special:
        basic_characters.extend(list("!#$%^&*(){}[]"))
    
    if numbers:
        basic_characters.extend(list("1234567890"))

    ## Recorrer elementos
    for x in range(lenght):
        generate_password = generate_password + random.choice(basic_characters)


    return render(request, "pages/password.html", { "password": generate_password })