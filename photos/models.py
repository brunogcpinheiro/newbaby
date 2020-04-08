from django.db import models

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=64)
    parents = models.CharField(max_length=100)
    category = models.CharField(max_length=64)
    claps = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.parents}"
