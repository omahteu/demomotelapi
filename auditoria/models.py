from django.db import models


class Auditoria(models.Model):
    objects = None
    tempo = models.CharField(max_length=5, blank=True)
    nome = models.CharField(max_length=100, blank=True)
    data = models.CharField(max_length=10, blank=True)
