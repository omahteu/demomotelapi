from rest_framework import serializers
from valor.models import Valores


class ValoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valores
        fields = "__all__"
