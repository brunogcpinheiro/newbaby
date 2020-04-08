from django.urls import path

from .views import index, gestante, newborn

app_name = "photos"
urlpatterns = [
    path("", index, name="index"),
    path("gestante/", gestante, name="gestante"),
    path("newborn/", newborn, name="newborn")
]
