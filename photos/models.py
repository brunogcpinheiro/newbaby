from django.db import models

# Create your models here.


class Photo(models.Model):
    titulo = models.CharField(max_length=64)
    responsaveis = models.CharField(max_length=100)
    categoria = models.CharField(max_length=64)
    palmas = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.titulo} - {self.responsaveis}"
