from django.urls import path
from .views import *


urlpatterns = [
    path('list/', ViewTours.as_view()),
    path('informer/popular/', PopularToursInformer.as_view()),
    path('informer/new/', NewToursInformer.as_view()),
    path('informer/upcoming/', UpcomingToursInformer.as_view()),
    path('information/<int:tour_id>/', TourInformation.as_view()),
]