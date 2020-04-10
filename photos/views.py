from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from .models import Foto, Categoria

# Create your views here.

app_name = "photos"


def index(request):
    return render(request, "galeria.html")


def gestante(request):
    return render(request, "gestante.html", {
        "pregnant_photos": Foto.objects.filter(categoria__nome__startswith="Gestante")
    })


def newborn(request):
    return render(request, "newborn.html", {
        "newborn_photos": Foto.objects.filter(categoria__nome__startswith="Newborn")
    })


def acompanhamento(request):
    return render(request, "acompanhamento.html", {
        "support_photos": Foto.objects.filter(categoria__nome__startswith="Acompanhamento")
    })


def festa(request):
    return render(request, "festa.html", {
        "party_photos": Foto.objects.filter(categoria__nome__startswith="Festa infantil")
    })


def parto(request):
    return render(request, "parto.html", {
        "born_photos": Foto.objects.filter(categoria__nome__startswith="Parto")
    })


def outros(request):
    return render(request, "outros.html", {
        "other_photos": Foto.objects.filter(categoria__nome__startswith="Outros")
    })
