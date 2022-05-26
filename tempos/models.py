from django.db import models


class Tempos(models.Model):
    objects = None
    troca = models.CharField(max_length=20, blank=True)
    desistencia = models.CharField(max_length=20, blank=True)
    limpeza = models.CharField(max_length=20, blank=True)
    faxina = models.CharField(max_length=20, blank=True)
    manutencao = models.CharField(max_length=20, blank=True)
