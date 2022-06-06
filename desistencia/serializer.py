from rest_framework import serializers
from desistencia.models import Desistencia


class DesistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desistencia
        fields = "__all__"
