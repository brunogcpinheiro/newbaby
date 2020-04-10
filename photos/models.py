from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nome}"


class Foto(models.Model):
    titulo = models.CharField(max_length=64)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="categorias")
    imagem = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return f"{self.titulo} - {self.responsaveis}"

    def delete(self, *args, **kwargs):
        self.imagem.delete()
        super().delete(*args, **kwargs)
