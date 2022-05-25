from django.db import models


class TabelaPreco(models.Model):
    objects = None
    tabela = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.tabela
