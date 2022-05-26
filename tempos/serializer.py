from rest_framework import serializers
from tempos.models import Tempos


class TemposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tempos
        fields = '__all__'
