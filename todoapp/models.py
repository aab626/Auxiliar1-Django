from django.db import models

from django.utils import timezone
from categorias.models import Categoria

# Create your models here.

class Tarea(models.Model):
    titulo = models.CharField(max_length=250) # varchar
    contenido = models.TextField(blank=True)
    fecha_creación = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    categoria = models.ForeignKey(Categoria, default="general", on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

