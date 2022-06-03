from django.db import models


class Dados(models.Model):
    objects = None
    codigo = models.CharField(max_length=5, blank=True)
    quarto = models.CharField(max_length=3, blank=True)
    camareira = models.CharField(max_length=50, blank=True)
    dia = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.codigo
