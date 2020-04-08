from django.shortcuts import render

# Create your views here.

app_name = "photos"


def index(request):
    return render(request, "galeria.html")
