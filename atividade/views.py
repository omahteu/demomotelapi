from rest_framework import viewsets
from atividade.models import Atividade
from atividade.serializer import AtividadeSerializer


class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
