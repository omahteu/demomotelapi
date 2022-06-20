from rest_framework import viewsets
from auditoria.models import Auditoria
from auditoria.serializer import AuditoriaSerializer


class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset = Auditoria.objects.all()
    serializer_class = AuditoriaSerializer
