from rest_framework import viewsets
from tempos.models import Tempos
from tempos.serializer import TemposSerializer


class TemposViewSet(viewsets.ModelViewSet):
    queryset = Tempos.objects.all()
    serializer_class = TemposSerializer
