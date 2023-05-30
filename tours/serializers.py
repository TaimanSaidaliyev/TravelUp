from rest_framework import serializers, generics
from .models import Tours


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = ('__all__')
        depth = 2


class InformerToursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = ('id', 'title', 'description', 'vip', 'category', 'price', 'image')
        depth = 2