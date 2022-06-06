from django.db import models


class Desistencia(models.Model):
    objects = None
    codigo = models.CharField(max_length=5, blank=True)
    quarto = models.CharField(max_length=3, blank=True)
    caixa = models.CharField(max_length=50, blank=True)
    motivo = models.TextField()

    def __str__(self):
        return self.codigo
