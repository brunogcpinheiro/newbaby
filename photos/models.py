from django.db import models

# Create your models here.


class Category(models.Model):
    nome = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nome}"


class Photo(models.Model):
    titulo = models.CharField(max_length=64)
    responsaveis = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories")
    imagem = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return f"{self.titulo} - {self.responsaveis}"

    def delete(self, *args, **kwargs):
        self.imagem.delete()
        super().delete(*args, **kwargs)
