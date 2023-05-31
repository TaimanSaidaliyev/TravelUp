from rest_framework import serializers, generics
from .models import *


class LocationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ('__all__')
        depth = 2