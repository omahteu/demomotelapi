from rest_framework import viewsets
from produtos.models import Produto
from produtos.serializer import ProdutoSerializer


class ProdutoViewSets(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
