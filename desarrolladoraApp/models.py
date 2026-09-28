from django.db import models
from django.utils import timezone

# Create your models here.
class desarrolladora(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="LA DESARROLLADORA")
    creado = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Creación")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table= "desarrolladora"
        verbose_name= "DESARROLLADORA"
        verbose_name_plural = "DESARROLLADORAS"
        ordering = ["nombre"]