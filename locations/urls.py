from django.urls import path
from .views import *


urlpatterns = [
    path('info/<int:location_id>/', LocationInfo.as_view()),
    path('list/', LocationList.as_view()),
    path('list/priority/', LocationListMain.as_view()),
]