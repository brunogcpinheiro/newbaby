from django.shortcuts import render

from .models import Photo, Category

# Create your views here.

app_name = "photos"


def index(request):
    return render(request, "galeria.html")


def gestante(request):
    return render(request, "gestante.html", {
        "pregnant_photos": Photo.objects.filter(categoria__nome__startswith="Gestante")
    })


def newborn(request):
    return render(request, "newborn.html", {
        "newborn_photos": Photo.objects.filter(categoria__nome__startswith="Newborn")
    })
