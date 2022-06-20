from django.db import models


class Auditoria(models.Model):
    objects = None
    tempo = models.CharField(max_length=5, blank=True)
