from rest_framework import viewsets
from desistencia.models import Desistencia
from desistencia.serializer import DesistenciaSerializer


class DesistenciaViewSet(viewsets.ModelViewSet):
    queryset = Desistencia.objects.all()
    serializer_class = DesistenciaSerializer
