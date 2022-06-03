from rest_framework import viewsets
from limpeza.models import Limpeza
from limpeza.serializer import LimpezaSerializer


class LimpezaViewSet(viewsets.ModelViewSet):
    queryset = Limpeza.objects.all()
    serializer_class = LimpezaSerializer
