from django.urls import path

from .views import index, gestante, newborn, acompanhamento, festa, parto, outros

app_name = "photos"
urlpatterns = [
    path("", index, name="index"),
    path("gestante/", gestante, name="gestante"),
    path("newborn/", newborn, name="newborn"),
    path("acompanhamento/", acompanhamento, name="acompanhamento"),
    path("festa/", festa, name="festa"),
    path("parto/", parto, name="parto"),
    path("outros/", outros, name="outros")
]
