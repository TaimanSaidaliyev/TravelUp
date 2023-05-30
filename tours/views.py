from .models import Tours
from rest_framework.views import APIView, Response
from .serializers import TourSerializer, InformerToursSerializer


class ViewTours(APIView):
    def get(self, request):
        tours = Tours.objects.all()
        return Response(TourSerializer(tours, many=True).data)


class PopularToursInformer(APIView):
    def get(self, request):
        tours = Tours.objects.all()[:5]
        return Response(InformerToursSerializer(tours, many=True).data)


class NewToursInformer(APIView):
    def get(self, request):
        tours = Tours.objects.all()[:5]
        return Response(InformerToursSerializer(tours, many=True).data)


class UpcomingToursInformer(APIView):
    def get(self, request):
        tours = Tours.objects.all()[:5]
        return Response(InformerToursSerializer(tours, many=True).data)


class TourInformation(APIView):
    def get(self, request, tour_id):
        tours = Tours.objects.get(pk=tour_id)
        return Response(TourSerializer(tours, many=False).data)
