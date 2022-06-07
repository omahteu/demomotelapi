from rest_framework import viewsets
from valor.models import Valores
from valor.serializer import ValoresSerializer


class ValoresViewSet(viewsets.ModelViewSet):
    queryset = Valores.objects.all()
    serializer_class = ValoresSerializer
