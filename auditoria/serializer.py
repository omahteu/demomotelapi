from rest_framework import serializers
from auditoria.models import Auditoria


class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditoria
        fields = "__all__"
