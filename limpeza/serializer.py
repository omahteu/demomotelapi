from rest_framework import serializers
from limpeza.models import Limpeza


class LimpezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limpeza
        fields = "__all__"
