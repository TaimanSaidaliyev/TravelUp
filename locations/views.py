from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import *
from .serializers import *


def if_empty(value, secondary):
    if value == None:
        value = secondary
        return value


class LocationInfo(APIView):
    def get(self, request, location_id):
        tours = Locations.objects.get(pk=location_id)
        return Response(LocationInfoSerializer(tours, many=False).data)


class LocationList(APIView):
    def get(self, request):
        length = request.query_params.get('length')
        tours = Locations.objects.all()[0:if_empty(length, 100)]
        return Response(LocationInfoSerializer(tours, many=True).data)


class LocationListMain(APIView):
    def get(self, request):
        tours = Locations.objects.all().filter(priority=True)[0:10]
        return Response(LocationInfoSerializer(tours, many=True).data)
