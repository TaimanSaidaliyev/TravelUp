from .models import Tours
from rest_framework.views import APIView, Response
from .serializers import TourSerializer, InformerToursSerializer
from locations.models import Locations
from utils.utils import if_empty


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


class TourListFilter(APIView):
    def get(self, request):
        location = request.query_params.get('location')
        region = request.query_params.get('region')
        agent = request.query_params.get('agent')
        category = request.query_params.get('category')
        limit = request.query_params.get('limit')
        default_limit = 100
        tours = Tours.objects.all()

        if (location):
            tours = tours.filter(locations=location)[0: if_empty(limit, default_limit)]
        if (region):
            tours = tours.filter(region=region)[0: if_empty(limit, default_limit)]
        if (agent):
            tours = tours.filter(agent=agent)[0: if_empty(limit, default_limit)]
        if (category):
            tours = tours.filter(category=category)[0: if_empty(limit, default_limit)]

        return Response(InformerToursSerializer(tours, many=True).data)
