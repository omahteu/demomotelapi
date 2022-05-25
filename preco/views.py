from rest_framework import viewsets
from preco.models import TabelaPreco
from preco.serializer import TabelaPrecoSerializer


class TabelaPrecoViewSet(viewsets.ModelViewSet):
    queryset = TabelaPreco.objects.all()
    serializer_class = TabelaPrecoSerializer
