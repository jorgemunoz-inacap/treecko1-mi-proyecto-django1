from django.db import models
from django.utils import timezone
from desarrolladoraApp.models import desarrolladora

# Create your models here.
class Juego(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="El juego")
    desarrolladora = models.ForeignKey(desarrolladora, on_delete=models.CASCADE, verbose_name="Desarrolladora")
    descripcion = models.CharField(max_length = 100, verbose_name="Es un juego")
    imagen = models.ImageField(upload_to="juegos/", verbose_name="foto")
    plataforma = models.CharField(max_length=100, verbose_name="Se juega en")
    tipo = models.CharField(max_length= 100, verbose_name= "Es de tipo")
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = "juegos"
        verbose_name = "Juego"
        verbose_name_plural ="Juegos"
        ordering= ["nombre"]
