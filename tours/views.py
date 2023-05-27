from django.shortcuts import render
from .models import Tours
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from .serializers import TourListSerializer


class ViewTours(APIView):
    def get(self, request):
        tours = Tours.objects.all()
        return Response(TourListSerializer(tours, many=True).data)
