from rest_framework import serializers
from preco.models import TabelaPreco


class TabelaPrecoSerializer(serializers.ModelSerializer):
    class Meta:
        model: TabelaPreco
        fields: '__all__'
