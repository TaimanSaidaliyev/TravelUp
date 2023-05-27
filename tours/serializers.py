from rest_framework import serializers, generics
from .models import Tours


class TourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = ('__all__')
        depth = 2