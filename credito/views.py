from rest_framework import viewsets
from credito.models import Credito
from credito.serializer import CreditoSerializer


class CreditoViewSet(viewsets.ModelViewSet):
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer
