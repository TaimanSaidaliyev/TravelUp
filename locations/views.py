from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import *
from .serializers import *


class LocationInfo(APIView):
    def get(self, request, location_id):
        tours = Locations.objects.get(pk=location_id)
        return Response(LocationInfoSerializer(tours, many=False).data)
